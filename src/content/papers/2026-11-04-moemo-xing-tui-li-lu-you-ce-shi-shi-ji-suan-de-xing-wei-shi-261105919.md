---
title: 'Routes of Reasoning: Reading and Reshaping Test-Time Compute in MoE Models'
title_zh: MoE模型推理路由：测试时计算的行为识别与无训练调控
authors:
- Shengjie Wang
- Mohsen Fayyaz
- Nanyun Peng
affiliations:
- University of California, Los Angeles
arxiv_id: '2611.05919'
url: https://arxiv.org/abs/2611.05919
pdf_url: https://arxiv.org/pdf/2611.05919
published: '2026-11-04'
collected: '2026-11-05'
category: LLM
direction: LLM推理优化 · MoE路由无训练调控
tags:
- MoE
- Reasoning Efficiency
- Test-time Optimization
- Router Probing
- Inference Steering
one_liner: 通过MoE路由器logits识别推理行为，无训练调整路由即可降低30%+推理token量且精度几乎无损失
practical_value: '- 业务若用MoE架构LLM做Agent规划、生成式推荐文案/Query改写，可先通过轻量路由探针定位冗余行为（如重复校验、无效规划）对应的专家，推理时直接抑制对应专家，无需训练即可降低30%+token成本，精度损失可控

  - 无训练的路由调控方法无需修改模型权重，仅需在推理层做路由得分修改，上线成本极低，适合业务快速迭代试错推理效率优化方案

  - 针对生成式推荐/搜索场景LLM生成冗余内容的问题，仅需标注少量推理轨迹的行为标签即可训练线性探针，无需全量微调大模型，数据成本低'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长推理链LLM普遍存在「过度思考」问题：得到正确答案后仍反复校验、重推导，浪费大量测试时算力，甚至可能因冗余推导引入错误。现有调控方法多为限制token总数、prompt引导，无法针对特定推理行为精准调控，效果有限。MoE架构的路由器天然具备行为关联的潜力，可作为低开销的推理调控入口。
### 方法关键点
- 将推理轨迹拆分为句子级片段，标注6类推理行为（规划、执行、重述、事实、反思、结论），每个token继承所属片段的行为标签
- 基于路由器logits训练轻量线性探针做行为分类，效果与残差流探针相当，但特征维度仅为后者的56%
- 跨数学、代码、科学、知识、常识5个领域验证，同一推理行为对应的专家集合可迁移，无需每个场景单独标注
- 推理时直接修改指定行为关联专家的路由得分，升高/降低对应专家的激活概率，无需微调模型权重
### 关键实验
在Gemma-4、Qwen3、Qwen3.6、GPT-OSS共4个开源MoE模型上测试，覆盖MATH500、AIME、GPQA、AICrypto 4个基准，对比原生模型、随机专家调控、简洁prompt三类基线：中位数减少30.4%生成token，最高降幅达63.3%；准确率最多下降0.5个百分点，14/16测试场景下准确率持平或提升。
### 核心结论
MoE路由器既是推理行为的可解释观测窗口，也是无训练优化测试时计算的轻量控制接口。
