---
title: 'SpecKCast: Spectral Kalman Forecasting for Diffusion Acceleration'
title_zh: SpecKCast：基于频谱卡尔曼预测的扩散Transformer推理加速方法
authors:
- Javad Rajabi
- Hakki Can Karaimer
- David B. Lindell
- Babak Taati
- Michael S. Brown
affiliations:
- University of Toronto
- Vector Institute
- Samsung Electronics
arxiv_id: '2610.26837'
url: https://arxiv.org/abs/2610.26837
pdf_url: https://arxiv.org/pdf/2610.26837
published: '2026-10-18'
collected: '2026-10-21'
category: Other
direction: 扩散模型推理 · 频域预测加速
tags:
- Diffusion Acceleration
- Kalman Filter
- Frequency Domain
- Inference Optimization
- DiT
one_liner: 训练无关的频域分带卡尔曼预测方法，实现扩散模型最高6倍加速，额外内存小于0.05GiB
practical_value: '- 做电商AIGC广告图/短视频业务的团队可直接集成SpecKCast，在几乎无额外内存开销的前提下将文生图/文生视频推理速度提升3-6倍，降低生成服务成本

  - 频域分带+任务专属时间轴扭曲的设计思路可迁移到推荐系统时序特征预测场景，比如用户兴趣演化预测、用户行为序列建模，对不同变化频率的特征分带建模提升预测精度

  - 基于预测不确定性的自适应调度策略可复用在大模型推理缓存、KV cache淘汰策略设计中，通过不确定性阈值决定是否触发重计算，平衡性能与效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
扩散Transformer（DiT）生成图像/视频质量高，但需多轮denoising迭代，推理延迟高，难以落地实时业务。现有缓存、预测类加速方法要么直接复用相邻步特征，加速比上限低；要么对所有特征统一做时序预测，忽略不同空间频率分量在denoising各阶段的演化差异，也未考虑denoising进度的非线性特性，跳步时误差快速放大，进一步限制了可实现的加速比。
### 方法关键点
- 频域分带建模：对DiT输出做2D DCT变换，按径向划分为多个频率带，不同带单独建模演化规律，适配低频先稳定、高频后演化的特性
- 带专属时间坐标：基于噪声调度的log SNR做非线性扭曲，生成每个频率带专属的时间轴，匹配不同带的活跃阶段，解决denoising进度非线性问题
- 轻量卡尔曼滤波：每个DCT系数用独立卡尔曼滤波跟踪值和变化率，同频率带共享协方差统计，几乎无额外计算与存储开销
- 不确定性驱动调度：当预测不确定性超过阈值时才触发DiT全量计算，自适应决定跳步长度，平衡加速比与生成质量
### 关键结果
在FLUX.1-dev、Qwen-Image、Wan2.1-14B、HunyuanVideo四个SOTA文生图、文生视频模型上，对比TaylorSeer、Spectrum、TeaCache等7个主流基线，最高实现6倍加速，额外内存开销小于0.05GiB；相同NFE下PSNR比最强基线高1.1~2.1dB，LPIPS低0.02~0.26，生成质量更接近50步全量推理结果。
> 最值得记住的结论：对时序信号按变化频率分带建模，匹配其演化规律做预测，能以极低开销大幅提升预测精度与加速比。
