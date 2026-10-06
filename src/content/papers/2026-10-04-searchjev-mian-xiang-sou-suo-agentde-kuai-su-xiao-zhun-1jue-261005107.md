---
title: 'SearchJev: A Fast and Calibrated System-1 Model for Search Agents'
title_zh: SearchJev：面向搜索Agent的快速校准System-1决策模型
authors:
- Congfeng Cao
- Lipeng Zuo
- Konstantinos Papakostas
- Qiwei Xu
- Songwei Xu
- Lun Zhou
- Zhaochun Ren
- Yougang Lyu
- Xiaohui Yan
affiliations:
- Huawei Technologies Co., Ltd.
- Leiden University
arxiv_id: '2610.05107'
url: https://arxiv.org/abs/2610.05107
pdf_url: https://arxiv.org/pdf/2610.05107
published: '2026-10-04'
collected: '2026-10-06'
category: Agent
direction: 搜索Agent双系统决策优化
tags:
- Search Agent
- System 1
- Calibration
- Dual System
- Decision Model
one_liner: 提出面向搜索Agent的校准型System-1决策模型，结合双系统架构同时提效提准
practical_value: '- 双系统Agent架构可直接复用：将高频短决策（如商品相关性判断、query改写校验、证据充足性判断）交给小参数量System1模型处理，置信度不足的case路由到大模型System2，兼顾效率与准确率，适合电商搜索、RAG问答场景降本提效

  - System1决策的工程优化trick可直接落地：跳过自回归生成环节，直接取LM首个输出token对应合法选项的logit做归一化输出决策，延迟可比同大小自回归模型降低80%以上，适配高并发的搜索/推荐实时判断场景

  - SLCD校准方法可迁移：用软标签+交叉熵+Brier损失联合训练，再按输出类型做温度校准，能降低40%-70%的预期校准误差，提升置信度判定的可靠性，减少大模型路由的误判

  - 多任务决策训练范式可复用：统一多类搜索决策的schema输入格式，用同一模型支持多任务判断，无需为每个决策任务单独训练模型，降低运维成本'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于LLM的搜索Agent用同一生成流程处理所有推理与决策，高频短决策（相关性判断、query改写校验、证据充足性判定等）的自回归生成带来大量延迟，且输出置信度校准误差高；单任务专用模型则需要为不同决策单独训练维护，部署成本高。
### 方法关键点
- 基于schema定义决策任务与合法选项，输入拼接搜索状态+任务说明+选项，直接取LM首个输出token对应选项标签的logit做归一化输出决策概率，无自回归生成开销
- 提出SLCD校准训练范式：用带不确定性的软标签做监督，交叉熵+Brier损失联合训练，再按输出类型（分类/打分/二分类）做温度校准，大幅降低置信度误差
- 双系统Agent架构：SearchJev处理所有短决策，置信度低于阈值的case路由到System2大模型处理，System2仅负责规划、query生成、答案合成
- 构建SearchDecision-Bench：统一6类搜索决策（路由/改写/相关性/充足性/导航/验证）的训练评估格式，覆盖ID/OOD测试集
### 关键实验
- 决策层：在SearchDecision-Bench上，SearchJev比同参数Qwen3.5自回归模型决策质量更高，速度快5.2~5.3倍，平均预期校准误差降低41%~74%
- 端到端Agent层：在BrowseComp-Plus数据集上，双系统Agent比纯27B System2方案搜索速度快3.7~4.7倍，答案准确率从45%提升至最高54%，System2输出token减少3.3~4.8倍
### 核心结论
搜索Agent的高频短决策与复杂推理解耦，用小模型做高效校准的System1决策、不确定case路由大模型的双系统架构，是兼顾效果、效率、成本的可行路径
