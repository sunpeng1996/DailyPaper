---
title: 'On the SPOT: Enhancing Speculative Decoding for Diffusion Language Models
  via Commit-Order Prediction'
title_zh: SPOT：基于提交顺序预测的扩散语言模型投机解码增强方法
authors:
- Eliezer Shlomi
- Eliron Rahimi
- Avi Mendelson
- Chaim Baskin
affiliations:
- Technion – Israel Institute of Technology
- INSIGHT Lab, Ben-Gurion University of the Negev
arxiv_id: '2610.22543'
url: https://arxiv.org/abs/2610.22543
pdf_url: https://arxiv.org/pdf/2610.22543
published: '2026-10-25'
collected: '2026-10-28'
category: LLM
direction: 扩散语言模型 · 推理加速
tags:
- Diffusion LM
- Speculative Decoding
- Inference Acceleration
- Commit Order Prediction
- Coupled Noise
one_liner: 面向扩散语言模型，用超轻量提交顺序预测模型+耦合噪声验证实现最高3.4倍无损推理加速
practical_value: '- 生成式推荐/Agent场景下的扩散类LLM推理加速可直接复用SPOT思路：0.62M超小参数的顺序预测模型仅依赖模型输出分布即可训练，推理
  overhead 可忽略，完全无损提升文案/应答生成速度

  - 跨模型迁移能力可复用：SPOT模型不依赖目标模型的内部结构或隐藏状态，无需微调即可在多款不同架构的扩散LM上实现加速，适合多模型部署的电商场景降本

  - 耦合噪声验证技术可迁移至需要保留生成多样性的场景（如个性化推荐文案生成、Agent多轮应答），在提速的同时完全保留原始模型的采样分布，不影响个性化效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
扩散语言模型（DLM）具备双向注意力、迭代修正、安全鲁棒性等优势，是下一代大语言模型的重要方向，但现有解码存在严重的速度-质量 trade-off：逐位置精确解码速度极慢，多token并行解码会损失生成质量；传统自回归模型的投机解码无法直接迁移到DLM，因为DLM需要同时决策「生成什么token」和「在哪个位置生成」，现有方案未解决提交顺序预测的核心瓶颈。
### 方法关键点
- 核心洞察：DLM上一轮前向的stale输出分布已经能覆盖92%以上最终提交的token，核心瓶颈是预测哪个位置会被优先提交，而非token预测
- 设计0.62M参数的轻量Transformer编码器，仅输入stale分布的统计特征，预测未来提交位置顺序，基于前缀质量构建多步候选状态树，目标模型单次批处理前向即可完成所有候选验证
- 提出耦合噪声验证机制：drafter和目标模型共享Gumbel噪声表，任意温度下的采样验证均为无损，完全保留原始模型的生成分布
- 扩展SPOT-Sets支持动态阈值解码，可同时预测多位置提交集，进一步提升吞吐
### 关键结果
在SDAR-8B等6款不同架构的DLM上测试，覆盖GSM8K、MBPP、HumanEval等基准任务，对比Spiffy、SSD、BlockSpec等所有主流baseline：
- SPOT相比标准解码最高减少6.8倍目标前向次数，吞吐提升最高3.4倍，比最优基线Spiffy吞吐高1.4倍
- SPOT checkpoint无需微调即可跨6款DLM迁移，性能损失仅4%~8%
- SPOT-Sets在动态阈值解码基础上平均再提升59%吞吐，SDAR-8B上平均达到标准解码7.9倍吞吐，完全无损

> 最值得记住的一句话：扩散语言模型投机解码的核心瓶颈不是token预测，而是提交顺序预测，仅靠超轻量的顺序预测模型就能实现数倍无损加速
