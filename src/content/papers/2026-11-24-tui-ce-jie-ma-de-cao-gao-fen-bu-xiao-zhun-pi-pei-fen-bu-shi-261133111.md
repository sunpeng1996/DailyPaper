---
title: 'Draft Calibration for Speculative Decoding: Accelerating LLM Serving by Matching
  Draft and Target Distributions'
title_zh: 推测解码的草稿分布校准：匹配分布实现LLM推理加速
authors:
- Yuxing Liu
- Wei Zuo
- Walid Krichene
- Tong Zhang
- Li Zhang
affiliations:
- UIUC
- Microsoft
arxiv_id: '2611.33111'
url: https://arxiv.org/abs/2611.33111
pdf_url: https://arxiv.org/pdf/2611.33111
published: '2026-11-24'
collected: '2026-11-25'
category: LLM
direction: LLM推理加速 · 推测解码校准
tags:
- Speculative Decoding
- Temperature Scaling
- LLM Inference
- Calibration
- Serving Efficiency
one_liner: 给推测解码的草稿模型加无开销温度缩放，最高提升10%接受长度
practical_value: '- 业务中用推测解码加速LLM服务（生成式推荐文案、Agent回复等）时，直接将草稿模型温度调至0.4-0.6区间，无额外开销即可提升5%-10%推理吞吐量

  - 自研蒸馏小模型做推理加速时，优先验证蒸馏模型的置信度偏差，通过温度缩放校准分布的投入产出比远高于修改模型结构或训练流程

  - 高并发LLM服务场景下优先选择链式推测解码+温度缩放的方案，相比树式推测解码在大batch下不会产生额外验证开销，稳定性更高'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
推测解码是LLM推理降本提效的核心工业级方案，加速上限由草稿模型生成token的目标模型接受率决定，接受率与草稿、目标模型的分布L1距离直接负相关。现有开源草稿模型普遍存在置信度偏低、分布更平坦的问题，与目标模型存在系统性分布差，此前研究多聚焦模型结构修改或训练流程优化，零开销的后处理校准路径未被充分挖掘。
### 方法关键点
- 验证EAGLE-3、DFlash、DSpark等主流开源草稿模型普遍对top1候选置信度低于目标模型，即使top候选预测正确，概率值也存在系统性偏差
- 优先测试标准温度缩放校准草稿分布：降低草稿模型温度锐化分布，完全不修改模型权重、无额外推理开销，不破坏推测解码的分布无损特性
- 进一步测试Dirichlet缩放、token自适应校准头等更细粒度校准方案，验证潜在提升空间
### 关键实验
覆盖数学、代码、对话8类基准数据集（GSM8K、MT-Bench、HumanEval等），基线为草稿温度与目标温度一致（Td=1）：
- 标准温度缩放可提升平均接受长度最高10%，服务吞吐量最高提升22%，全局Td设为0.4-0.6即可覆盖绝大多数场景的最优效果，任务级单独调优增益不足1%
- 更细粒度的后处理校准方法当前无法超过温度缩放的效果，token自适应校准存在理论提升空间但现有落地方案无法兑现
### 核心结论
推测解码的草稿模型无需与目标模型使用相同温度，调低草稿温度即可实现几乎零成本的服务效率提升
