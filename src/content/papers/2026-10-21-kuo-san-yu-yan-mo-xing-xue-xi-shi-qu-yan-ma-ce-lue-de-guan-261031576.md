---
title: What Makes a Good Unmasking Policy? A Controlled Study of Learned Unmasking
  in Diffusion Language Models
title_zh: 扩散语言模型学习式去掩码策略的关键设计因素对照研究
authors:
- Jinya Sakurai
- Xun Xu
- Jaehong Yoon
affiliations:
- NTU Singapore
- Institute for Advanced Intelligence and Computing (A*STAR)
- Centre for Frontier AI Research (A*STAR)
arxiv_id: '2610.31576'
url: https://arxiv.org/abs/2610.31576
pdf_url: https://arxiv.org/pdf/2610.31576
published: '2026-10-21'
collected: '2026-10-23'
category: LLM
direction: 扩散大语言模型 · 解码效率优化
tags:
- Diffusion LLM
- Unmasking Policy
- Decoding Acceleration
- Lightweight Policy
- Throughput Optimization
one_liner: 通过对照实验明确扩散语言模型去掩码策略最优设计，提出856K轻量策略实现精度-吞吐最优权衡
practical_value: '- 生成式推荐/文案场景的推理加速参考：若采用dLLM做商品文案、query推荐生成，可直接复用856K参数量级的轻量去掩码策略设计，仅需降低10%的主模型调用次数即可获得端到端吞吐提升，无需大幅增加推理成本

  - 序列决策类任务的监督信号设计：做token级动态决策（如生成截断、劣质token过滤）时，避免仅用最终输出匹配做标注，可引入轨迹收缩思路，仅保留能落到最优生成路径上的正例，提升低迭代次数场景的生成质量

  - 多特征融合trick：单独用大模型隐状态做轻量策略输入效果差，和token置信度、概率margin等统计特征结合可实现效果增益，可复用在召回排序的轻量打分、生成式推荐的结果校验等场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
扩散语言模型（dLLM）支持并行生成，比自回归模型具备更高的推理效率潜力，但去掩码策略直接决定其精度-效率权衡。现有学习式去掩码策略的监督信号、输入特征、参数量等维度混合优化，无法明确各因素的实际贡献，难以指导工业落地的策略设计。
### 方法关键点
1. 从蒸馏视角拆分去掩码策略核心设计维度，开展单变量对照实验，排除混杂因素干扰；
2. 提出轨迹收缩监督标签，仅允许提交能落到参考轨迹后续状态的token，解决仅匹配最终输出的过宽松问题；
3. 输入采用置信度+backbone隐状态的组合，搭配856K参数的轻量DiT结构策略网络，参数量仅为backbone的0.01%；
4. 明确轻量策略的盈亏平衡点：7.5M以内的策略仅需降低10%的主模型调用次数（NFE），即可抵消额外开销。
### 关键实验结果
在LLaDA-8B-Instruct、Dream-7B-Instruct两个dLLM backbone上测试，对比Fast-dLLM、Learn2PD等基线：GSM8K任务98%精度目标下，TPS比最优基线高42.7%；MATH-500、HumanEval中等精度目标下NFE最少，跨backbone、跨128/256/512生成长度泛化性良好。
### 最值得记住的一句话
轻量学习式辅助策略的收益核心是在可控开销下降低主模型的调用次数，而非追求策略本身的高精度。
