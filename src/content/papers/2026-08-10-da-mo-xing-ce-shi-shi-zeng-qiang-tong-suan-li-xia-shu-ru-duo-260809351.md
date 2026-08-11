---
title: 'Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity
  at Matched Compute'
title_zh: 大模型测试时增强：同算力下输入多样性优于输出多样性
authors:
- Nikita Kozodoi
- Zainab Afolabi
- Jack Butler
affiliations:
- Amazon Web Services
arxiv_id: '2608.09351'
url: https://arxiv.org/abs/2608.09351
pdf_url: https://arxiv.org/pdf/2608.09351
published: '2026-08-10'
collected: '2026-08-11'
category: LLM
direction: LLM测试时增强 · 推理效率优化
tags:
- Test-Time Augmentation
- Self-Consistency
- Inference Efficiency
- LLM Reasoning
- Prompt Robustness
one_liner: 同算力约束下对比LLM测试时输入输出多样性，证明语义TTA性价比更高
practical_value: '- 电商搜索/推荐的Query理解、用户意图分类场景可直接复用语义TTA策略：对用户Query生成4个同义重述版本分别推理，多数投票输出结果，同等算力下单位美元准确率增益是self-consistency的1.8倍

  - 成本敏感的LLM Agent/客服机器人部署场景优先选择k=4的语义TTA，无需训练即可提升中低端LLM推理准确率；若基线模型准确率已达85%以上，TTA增益<0.5pp可直接放弃

  - 多模态商品理解/图文搜索场景仅对文本Query做语义重述即可，无需同时对商品图像做旋转、亮度调整等视觉增强，两者叠加会引入噪声反而降低准确率

  - 极致成本约束场景可替换为词汇TTA：对Query做5%概率的字符级扰动，无额外重述LLM调用成本，效果接近self-consistency基线'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前LLM推理侧提准方案多集中在输出侧（如self-consistency多推理路径采样），但每增加一次推理调用都会直接提升部署延迟与成本，单位算力的准确率增益是业务落地的核心指标。输入侧Test-Time Augmentation（TTA）在CV、监督NLP任务中已验证有效，但尚未在生成式LLM场景下做系统的同算力对比，无法明确输入与输出侧多样性哪种更具性价比。
### 方法关键点
- 三类TTA策略：1）语义TTA：单次调用LLM生成k个保留原意、格式的Query重述版本，分别推理后通过多数投票聚合结果；2）词汇TTA：对Query做5%概率的字符级增删改、拼写错误注入，无额外LLM调用成本；3）视觉TTA：对多模态输入的图像做±3°旋转、±5%亮度/对比度调整。
- 对比基线为单轮CoT推理、self-consistency（同输入采样k条推理路径投票），所有对比严格控制推理调用次数，保证算力匹配。
### 关键实验
覆盖MMLU、Math500、多模态MMMU等6个通用/专业/多模态任务，基于Claude 4.5系列模型测试：
- 语义TTA在5/6任务上优于self-consistency，平均准确率提升1.8pp，单位美元准确率增益是self-consistency的1.8倍，统计显著（p<0.05）。
- 语义TTA最优k均值为4.33，比self-consistency需要更少样本即可达到准确率峰值；中端模型增益最高（Haiku提升2.75pp，旗舰Opus仅提升0.25pp）。
- 多模态场景下仅文本语义TTA效果最优，同时叠加文本+视觉增强反而比单轮CoT基线准确率低1pp。
### 核心结论
对于当前中端LLM，在无法负担更大模型的场景下，调整输入比单纯调整推理路径能更高效地将推理算力转化为准确率。
