---
title: Speculative Diffusion is a Tale of Two Tradeoffs
title_zh: 投机扩散解码的双重权衡优化研究
authors:
- Aaron Zorel
- Guy Van den Broeck
- Aditya Grover
- Daniel Israel
affiliations:
- Independent Researcher
- University of California, Los Angeles
arxiv_id: '2610.31819'
url: https://arxiv.org/abs/2610.31819
pdf_url: https://arxiv.org/pdf/2610.31819
published: '2026-10-21'
collected: '2026-10-27'
category: LLM
direction: LLM推理加速 · 投机扩散解码
tags:
- speculative_decoding
- diffusion_LLM
- inference_optimization
- pareto_frontier
- lossy_decoding
one_liner: 联合调整扩散草稿步数与验证宽容度，拓展LLM投机解码的速度-质量帕累托边界
practical_value: '- 做LLM驱动的智能客服、商品文案生成、Agent推理场景时，可基于业务对质量/延迟的容忍度，联合调整扩散草稿模型步数和验证宽容度，在不显著影响业务效果的前提下降低推理成本

  - 对于需要高吞吐的推荐系统侧边栏生成、搜索query补全场景，可优先选用低扩散步数+高宽容度的配置，实测最高可提升10x以上生成速度

  - 复用论文提出的线性插值接受准则，无需修改模型结构即可实现无损到有损推理的平滑切换，适配不同等级的SLA要求

  - 无专用扩散草稿模型的场景，可直接用通用多步扩散LLM作为草稿，配合动态调参即可达到接近专用单步草稿的帕累托表现'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统投机解码要么保证无损但速度上限受草稿模型与验证模型的拟合度约束，要么采用有损策略仅调整验证接受规则，而扩散LLM作为草稿模型本身就存在扩散步数（计算量）和生成质量的固有权衡，过往研究未对扩散步数、验证宽容度两个维度做联合优化，导致无法触达全局最优的速度-质量帕累托边界。
### 方法关键点
- 理论证明：固定提议分布下，验证分布与草稿分布的线性插值是总变差偏差约束下接受率最高的最优验证策略
- 工程简化：多步扩散草稿的投机解码可直接采用扩散最后一步的输出概率作为提议概率，无需计算不可行的轨迹边际概率即可保证分布正确性
- 量化模型：建立吞吐量预测模型，明确扩散步数K、接受宽容度λ两个参数对生成速度、输出质量的量化影响关系
### 关键结果
在GSM8K（数学推理）、GPQA（知识问答）、HumanEval（代码生成）三个基准数据集上测试，联合调整两个参数相比仅调整单一参数，可将帕累托边界拓展22%；同精度下生成延迟降低35%，同延迟下任务准确率提升17%；扩散草稿的最高生成速度可达纯自回归验证模型的10倍以上。
**核心结论**：投机扩散解码没有全局最优的单参数配置，需根据业务对延迟、质量的容忍度联合调整扩散计算量和验证宽松度
