---
title: 'LocUS: Head Selection and Subspace Projection for Targeted Activation Steering'
title_zh: LocUS：基于注意力头选择与子空间投影的LLM定向激活调控方法
authors:
- Irene Tallini
- Lorenzo Basile
- Valentino Maiorca
- Francesco Locatello
- Alberto Cazzaniga
affiliations:
- Area Science Park, Trieste, Italy
- Institute of Science and Technology Austria
- Université Côte d'Azur, Inria, France
arxiv_id: '2609.31122'
url: https://arxiv.org/abs/2609.31122
pdf_url: https://arxiv.org/pdf/2609.31122
published: '2026-09-25'
collected: '2026-09-28'
category: LLM
direction: LLM无训练激活调控 · 注意力头筛选
tags:
- ActivationSteering
- AttentionHead
- SubspaceProjection
- LLMAlignment
- InferenceOptimization
one_liner: 通过词法子空间约束与稀疏注意力头筛选实现LLM定向激活调控，效果优于SOTA且保留通用能力
practical_value: '- 电商文案/客服LLM的可控性优化：针对"语气友好""规避合规风险""统一营销话术"等需求，无需全量/ LoRA微调，仅需准备少量对比样本、定义目标属性词表，复用LocUS的头筛选+子空间投影逻辑做推理时激活注入，成本远低于微调，且不影响模型常识应答能力

  - 导购Agent行为对齐：针对Agent需避免过度推销、规避竞品提及、拒绝违规请求等场景，用LocUS可在不修改模型权重的前提下实现稳定的行为约束，比prompt
  engineering鲁棒性更高，无prompt泄露风险

  - 工程落地可复用trick：EVR头筛选规则（μ+2σ阈值）无需人工枚举层/头参数，SOMP稀疏重建逻辑可直接嵌入现有LLM推理框架的hook机制，额外推理开销<5%，适合在线部署'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有无训练LLM激活调控方法（如DoM）基于对比样本估计全层调控向量，容易继承数据中的非目标属性偏差，导致模型通用能力（事实性、推理、生成流畅度）大幅下降；现有头选择的调控方案要么仅适配特定属性，要么需人工扫参，同时未对调控向量做子空间约束，仍会引入无关特征。
### 方法关键点
- 基于目标属性的关键词集合，从LLM的unembedding矩阵中抽取对应列作为词法原子字典，锚定模型解码目标属性的激活方向
- 用SOMP稀疏重建每个注意力头的输出，计算解释方差比（EVR），自动筛选EVR高于全局均值+2倍标准差的头作为干预位点，仅占总头数的6%以内
- 将DoM估计的调控向量投影到每个筛选头的专属词法子空间，仅修改和目标属性直接相关的激活分量，隔绝无关特征
- 自动校准调控强度，保证生成PPL不超过未干预模型的2倍、MMLU不低于未干预模型的99%
### 关键实验结果
在毒性降低、情感转向、阿谀奉承抑制3类任务上，测试Mistral-7B、DeepSeek-7B、Llama-8B、DeepSeek-67B共4个模型，对比DoM、ITI、SMH等SOTA基线：8/9的任务场景下调控效果优于基线，毒性最高降92%、情感转向准确率最高达99%、阿谀奉承行为最高降74%；MMLU基本与未干预模型持平，仅使用0.4%-0.8%的全层DoM调控自由度；跨数据集迁移性优异，基于Jigsaw数据集训练的毒性调控器在TET数据集上比DoM最高多降10%的毒性。
### 最值得记住的结论
激活调控的核心是定位模型输出目标属性的位点和方向，而非仅能检测到属性的位点，才能以最小干预实现最高调控精度与最低能力损耗。
