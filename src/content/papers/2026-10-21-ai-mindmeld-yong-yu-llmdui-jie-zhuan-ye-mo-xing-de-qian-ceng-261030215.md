---
title: 'AI Mindmeld: A Latent Interconnect Protocol'
title_zh: AI Mindmeld：用于LLM对接专业模型的潜层互连协议（LIP）
authors:
- Siavash Golkar
- Jake Kovalic
- Shirley Ho
affiliations:
- Polymathic AI
- 纽约大学数据科学中心
- 耶鲁大学应用物理系
- Flatiron研究所计算天体物理中心
- 普林斯顿大学天体物理科学系
arxiv_id: '2610.30215'
url: https://arxiv.org/abs/2610.30215
pdf_url: https://arxiv.org/pdf/2610.30215
published: '2026-10-21'
collected: '2026-10-23'
category: Agent
direction: LLM Agent 多模型隐层互连协议
tags:
- LLM Agent
- Latent Representation
- Protocol
- Tool Use
- Model Alignment
one_liner: 提出冻住基座与专业模型、仅训练跨层连接器的潜层互连协议，实现多模型无联合训练的隐式信息互通
practical_value: '- 电商/广告推荐Agent对接召回、排序、用户画像等垂直模型时，可复用冻住基座LLM仅训练轻量跨层连接器的方案，避免反复微调基座带来的成本和性能退化风险

  - 多源信息融合场景可参考分层注入隐层表示的思路：将用户行为Embedding、商品Embedding直接注入LLM中间层，比转为文本输入的信息带宽更高，还能支撑零样本跨任务迁移

  - 搭建多模型统一调用框架时可参考LIP的注册表设计：各垂直模型的连接器独立训练注册，新增模型无需改动现有链路和基座，大幅提升扩展性'
score: 9
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有LLM Agent的工具调用链路只能通过文本、图像等人类可理解格式传递信息，存在严重带宽瓶颈：专业模型（如推荐系统的召回/排序模型、用户画像模型）的高维隐层表征中包含大量未被显式描述的信息，转成文本会丢失大量有效信号。同时现有多模型对接方案要么需要微调LLM基座，要么仅能在输入层注入表征，扩展性、灵活性、组合性差，无法支撑多专业模型无联合训练的协同工作。
### 方法关键点
- 提出Latent Interconnect Protocol（LIP），全程冻结预训练LLM和所有专业模型，仅训练轻量connector实现专业模型表征到LLM内部状态的映射，适配成本极低
- 支持将专业表征注入LLM多个中间层而非仅输入层，通过标准化混合算子将专业表征与LLM原生残差状态融合，信息利用效率更高
- 采用注册表机制管理所有connector，新增专业模型仅需单独训练对应connector，无需改动LLM或已有connector，多个独立训练的connector可在推理时自由组合
### 关键实验结果
对接3个蛋白、3个小分子专业模型到Gemma 3 4B、Gemma 3 12B、Kimi K2.6三个LLM：
1. 已知任务未知对象的预测AUROC：Kimi K2.6上蛋白领域平均0.92~0.93，小分子领域0.87~0.93
2. 未知任务未知对象的零样本迁移AUROC：Kimi K2.6上蛋白领域平均0.86，小分子领域平均0.74，性能随LLM能力提升单调增长
3. 跨领域零样本组合任务（蛋白-小分子结合预测）：使用4 token MLP connector时Kimi K2.6的排序准确率可达0.8
### 核心结论
直接在LLM中间层注入专业模型的高维隐层表征，比转成文本输入的信息传递效率高得多，且无需对基座LLM做任何修改
