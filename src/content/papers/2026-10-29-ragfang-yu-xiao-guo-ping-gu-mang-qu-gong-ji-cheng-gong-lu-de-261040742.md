---
title: 'Prevented is Not Protected: What Attack Success Rate Hides about RAG'
title_zh: RAG防御效果评估盲区：攻击成功率指标掩盖的真实风险
authors:
- Chahana Dahal
- Zuobin Xiong
affiliations:
- University of Nevada, Las Vegas
arxiv_id: '2610.40742'
url: https://arxiv.org/abs/2610.40742
pdf_url: https://arxiv.org/pdf/2610.40742
published: '2026-10-29'
collected: '2026-11-02'
category: Eval
direction: RAG安全 · 防御效果评估
tags:
- RAG
- Security
- Evaluation
- Knowledge Poisoning
- Defense
one_liner: 提出对齐式RAG评估框架，揭示仅用攻击成功率评估防御的多重盲区
practical_value: '- 评估业务RAG系统（如商品问答、客服知识库）的防御效果时，可复用「干净无防御/干净加防御/中毒无防御/中毒加防御」四组对照框架，同时统计拦截率、新引入错误率、干净查询准确率变化三个维度，避免仅靠攻击拦截率高估防御效果

  - 若业务RAG的检索来源包含可公开编辑的UGC内容（如商品评价、用户晒单），需注意基于检索分差/离散度的恶意内容检测器在检索结果中恶意内容占比超50%时会完全失效，建议补充多段内容一致性校验逻辑

  - 评估RAG内容注入攻击成功率时，不要仅用目标字符串匹配，可采用LLM judge判断模型是否实际认同恶意内容，避免将模型提及但明确否定的内容误判为攻击成功'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG知识投毒防御的评估仅依赖攻击成功率（ASR）指标，仅统计被拦截的攻击数量，完全忽略防御可能引入的新错误、对干净查询的负面影响，以及模型只是提及而非认同恶意目标的情况，导致防御效果评估严重失真，无法反映系统真实安全性。

### 方法关键点
- 设计四组对照的对齐评估协议：对同一查询固定目标、模型、解码策略，分别生成「干净检索无防御/干净检索加防御/中毒检索无防御/中毒检索加防御」四类结果，综合计算净攻击减少量、干净查询错误增量、因子对比度三个核心指标，同时统计防御拦截的攻击和新引入的攻击
- 新增检索依赖校验：通过移除中毒段落、保留单段中毒内容等对照实验，判断攻击成功是依赖单段中毒内容还是需要结合合法内容，还设计了需要同时结合合法和中毒内容才能触发的split-knowledge探针，用于分析内容组合类攻击
- 采用双维度打分：同时用字符串匹配和LLM judge两种方式判定攻击成功，区分模型提及恶意目标和实际认同恶意目标的差异

### 关键实验
在HotpotQA、Natural Questions两个公开数据集上，针对PoisonedRAG攻击，对比KeywordAgg、TrustRAG、提示词控制三类主流防御的效果。核心数字：1）TrustRAG在HotpotQA单段中毒场景下拦截20个攻击同时新增20个攻击，净效果为0；2）打分方式直接改变防御排名，同一份结果下字符串匹配显示TrustRAG和无防御效果一致，LLM judge则显示TrustRAG将攻击成功率从35%降到11%；3）检索分差类检测器在单段中毒时拦截率达98%，在5段中毒（检索结果全是恶意内容）时拦截率降到0。

最值得记住的一句话：RAG防御的真实效果不能仅看拦截了多少攻击，还要看它引入了多少新风险、对正常业务的影响有多大，「拦截了攻击」不等于「系统更安全」
