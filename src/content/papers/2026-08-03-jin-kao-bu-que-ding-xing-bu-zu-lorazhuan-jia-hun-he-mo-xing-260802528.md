---
title: 'Uncertainty Is Not Enough: Value-of-Information Routing for Mixtures of LoRA
  Experts'
title_zh: 仅靠不确定性不足：LoRA专家混合模型的信息价值路由机制
authors:
- Tom Saliencro
- Rohan Desai
- Priya Nair
- Maya Lindqvist
- Daniel Whitmore
affiliations:
- University of California, Irvine
- University of Washington
arxiv_id: '2608.02528'
url: https://arxiv.org/abs/2608.02528
pdf_url: https://arxiv.org/pdf/2608.02528
published: '2026-08-03'
collected: '2026-08-04'
category: Training
direction: MoE-LoRA 动态路由与计算优化
tags:
- LoRA
- MoE
- Dynamic Routing
- Value-of-Information
- Calibration
- Efficient Inference
one_liner: 提出VI-MoLE路由框架，通过量化增量风险收益全局分配LoRA专家预算，提升同算力下模型表现
practical_value: '- 垂直场景多LoRA专家部署（如电商分品类/场景LoRA适配器）可复用「边际收益/成本比」全局调度逻辑，替代固定top-k路由，同算力下提升推理效果

  - 电商/推荐的高风险场景（商品问答、合规内容生成）可借鉴校准残余风险证书机制，对高风险请求直接拒答或转人工，降低badcase率

  - 可复用反事实残余风险预测头的设计，仅用预获取特征就能判断下一个LoRA是否带来收益，避免无效计算，降低推理延迟'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前MoE-LoRA动态路由普遍遵循「不确定性越高、激活专家越多」的策略，存在本质缺陷：不确定性分为可还原（调用额外专家可消解）和不可还原（所有专家均判定输入歧义，增加专家无收益）两类，现有方法无法区分，导致算力浪费在无效调用上，同算力下性能天花板较低。
### 方法关键点
- 训练轻量风险头预测每个专家前缀的反事实残余风险，量化调用下一个专家能带来的边际风险降低幅度
- 基于独立校准集构造统一的风险上界证书，消除点估计误差，保障风险估计的统计有效性
- 全局调度计算预算，每次选择单位成本下认证边际收益最高的token/层位置调用专家，直到预算耗尽或无正收益
- 最终基于终端残余风险证书决定输出或拒答，兼顾效果和可靠性
### 关键结果
在8个通用常识推理数据集上与11个主流MoE-LoRA路由基线做同算力对比：
- 平均准确率较最优基线CARE高0.6pp，平均调用专家数少1%，预期校准误差（ECE）降低17.6%，风险覆盖率曲线下面积（AURC）降低12.1%
- 带风险控制的拒答模式下，目标风险违反率仅4%，较熵门控方法低16pp，覆盖度高0.6pp
- 分布偏移场景下仍保持90%左右的证书覆盖率，预算漂移不超过5%

**核心结论**：不确定性的大小不等于可还原性，动态资源分配的核心是判断下一份计算的边际收益，而非当前不确定性的高低。
