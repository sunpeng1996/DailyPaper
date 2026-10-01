---
title: 'PatchHolmes: Agentic Patch Retrieval via Listwise Selection'
title_zh: PatchHolmes：基于列表式选择的智能补丁检索Agent
authors:
- Guanqun Yang
- Yingming Zhou
- Jiangrui Zheng
- Shudong Hao
- Xueqing Liu
affiliations:
- Stevens Institute of Technology
arxiv_id: '2609.38807'
url: https://arxiv.org/abs/2609.38807
pdf_url: https://arxiv.org/pdf/2609.38807
published: '2026-09-30'
collected: '2026-10-01'
category: Agent
direction: Agent 垂直领域列表式检索优化
tags:
- Agent
- Listwise Ranking
- Retrieval
- RRF
- LLM
- Vulnerability Management
one_liner: 提出两阶段智能补丁检索系统，靠列表式Agent选择大幅超越点式基线性能
practical_value: '- 召回排序两阶段架构可直接复用：第一阶段用BM25+时间衰减+稠密向量RRF融合做粗召拿TopN候选，第二阶段Agent做精排，适合电商商品/广告候选池的精准排序场景，无需全量调用LLM大幅降本

  - 列表式选择比点式打分性价比更高：给Agent全量候选列表再选择性精读TopK，比逐个给候选独立打分少用7倍token的同时提升25%+Recall@1，可迁移到搜索推荐精排环节解决多候选打分平票问题

  - 垂直领域优先验证基座Embedding效果：通用检索Embedding榜单最优的LoRA微调模型在补丁检索场景下Recall@1掉了30%+，电商/推荐场景做召回不要盲目追通用榜单，优先在自有业务数据上做验证

  - Agent工具设计要极简：仅保留候选列表查询、多粒度内容读取、结果提交3类核心工具，多余工具会提升上下文溢出概率，落地业务Agent时可参考该裁剪思路'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
主流漏洞数据库中60%~63%的CVE缺失补丁链接，手动匹配效率低无法规模化；传统补丁检索采用点式独立打分，存在长diff截断、候选平票无法区分、召回率低的问题，且依赖微调或付费外部API成本高，急需可落地的低成本高准确率方案。

### 方法关键点
- 两阶段架构：第一阶段混合粗召，融合带时间衰减的BM25、Qwen3-Embedding-8B稠密检索结果，用RRF得到Top100候选；第二阶段Agent列表式精排，仅用1次会话从候选中选出最优补丁。
- 4个极简Agent工具：`list_candidates`（查看所有候选概览）、`read_commit`（8K字符粒度读取提交内容）、`read_file_diff`（16K字符粒度读取单文件diff）、`submit_answer`（提交结果），Agent最多迭代15轮，平均仅读取3~10个候选。
- 无微调无外部依赖：全流程用冻结开源LLM，跑在本地仓库，不需要针对每个场景微调也不需要调用外部搜索API。

### 关键实验
在GitHubAD数据集上，Recall@1达59.95%，比点式基线Favia高25.34%，比IRCoT基线高31.40%，仅用Favia 1/7的token量；相同候选集下，Agent比直接取粗召Top1提升27.32% Recall@1；迁移到PatchFinder_top10数据集无修改，Recall@1从24.28%提升到39.86%，覆盖71.4%的理论上限；同模型家族内换LLM，Recall@1波动小于1%，增益主要来自架构而非大模型本身。

### 核心结论
对于固定候选池的精准选择类任务，列表式Agent架构带来的性能增益远高于更换更大的LLM底座，且成本更低
