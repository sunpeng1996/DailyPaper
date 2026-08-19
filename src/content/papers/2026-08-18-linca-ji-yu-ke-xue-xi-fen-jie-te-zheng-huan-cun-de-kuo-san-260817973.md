---
title: 'LinCa: Accelerating Diffusion Models via Learnable Decomposed Feature Caching'
title_zh: LinCa：基于可学习分解特征缓存的扩散模型加速方法
authors:
- Jinshan Liu
- Haoran Qin
- Xiaobing Tu
- Jiacheng Liu
- Jiahui Hu
- Zhengan Yan
- Yukun Xie
- Kerui Shen
- Jinkui Ren
- Yuqi Lin
affiliations:
- Shanghai Jiao Tong University
- Alibaba Cloud Terminal Intelligent Computing Division
- Xi'an Jiaotong University
- Shandong University
- South China University of Technology
arxiv_id: '2608.17973'
url: https://arxiv.org/abs/2608.17973
pdf_url: https://arxiv.org/pdf/2608.17973
published: '2026-08-18'
collected: '2026-08-19'
category: Other
direction: 扩散模型推理 · 可学习特征缓存优化
tags:
- Diffusion Acceleration
- Feature Caching
- Invertible Network
- Inference Optimization
- Generative AI
one_liner: 用轻量可逆网络做特征分阶缓存，实现扩散模型5-7倍近无损推理提速
practical_value: '- 电商AIGC场景（商品主图/短视频生成、营销素材创作、虚拟主播内容生成）可直接复用LinCa框架，在几乎不损失生成质量的前提下将推理速度提升5-7倍，大幅降低服务部署成本与用户等待时延

  - 特征分解+差异化预测的思路可迁移到LLM推理的KV cache优化场景：将KV特征按连续性拆分，稳定维度做高阶预测、突变维度直接复用，平衡推理速度与输出精度，适合推荐Agent、对话Agent的大模型推理优化

  - 轻量可逆网络的适配思路可复用在端侧生成类模型优化上，仅需<0.2%额外参数、单卡1小时训练即可完成新模型适配，无需重训原大模型，落地成本极低'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有扩散模型特征缓存方法默认所有特征、所有阶段的演化规律一致，采用统一预测策略，无法适配跨模型、跨timestep、跨特征维度的动态异质性，高加速比下生成质量劣化严重，成为AIGC落地的核心性能瓶颈。
### 方法关键点
- 采用**Decompose-Predict-Reconstruct**流水线：用轻量可逆网络将缓存特征拆分为3个连续性不同的子分量，不稳定分量直接复用最近缓存，中高连续性分量分别用1阶、2阶Hermite插值预测，可逆网络的严格数学可逆性保证重构无信息损失
- 按timestep分段训练独立同构预测器，仅需100-200条预生成特征数据、单12GB GPU 1小时即可完成训练，新增参数量不到原模型的0.2%，推理开销可忽略
- 完全兼容蒸馏、量化等其他加速方案，可叠加使用实现更高加速比
### 关键结果
在FLUX.1-dev、Qwen-Image、HunyuanVideo、Qwen-Image-Edit等主流生成模型上对比TaylorSeer、FoCa、HyCa等SOTA缓存方案：实现5.51×（FLUX）、6.95×（Qwen图像生成）、5.50×（混元视频）、7.08×（Qwen图像编辑）加速，ImageReward、CLIP Score、VBench等指标均优于所有基线，生成质量接近无损。
> 值得记住的结论：特征维度的连续性异质性是缓存优化的核心抓手，可学习无损分解+差异化预测的范式可广泛复用在各类迭代式生成模型的推理加速场景。
