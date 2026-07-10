---
title: 'CineMobile: On-Device Image-to-Video Diffusion for Cinematic Camera Motion
  Generation'
title_zh: CineMobile：端侧图像转视频扩散模型实现电影级运镜生成
authors:
- Xuyao Huang
- Zelai Deng
- Xu Wang
- Xizhong Xiao
- Zhijie Deng
affiliations:
- Shanghai Jiao Tong University
- Nankai University
- Transsion
arxiv_id: '2607.03803'
url: https://arxiv.org/abs/2607.03803
pdf_url: https://arxiv.org/pdf/2607.03803
published: '2026-07-03'
collected: '2026-07-10'
category: Multimodal
direction: 端侧多模态生成 · 扩散模型压缩优化
tags:
- Diffusion Model
- On-Device AI
- Model Compression
- Image-to-Video
- DiT
one_liner: 提出三重优化的端侧图像转视频扩散框架，实现40倍提速，可在移动端生成电影级运镜视频
practical_value: '- 端侧生成类业务（如电商商品展示动效、买家秀短视频生成）可复用「蒸馏引导剪枝+扩散蒸馏+混合量化」的三重压缩流程，在效果无损前提下大幅降低推理时延

  - 扩散类生成模型落地端侧时，可参考4步蒸馏+RL优化思路，把多步去噪的迭代开销压到最低，适配移动端算力约束

  - 电商UGC内容工具类产品可直接借鉴该方案，给用户提供一键生成商品电影级展示视频的能力，降低内容创作门槛'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
移动端对图像转视频生成（尤其是子弹时间、滑动变焦等电影级运镜效果）需求旺盛，但DiT结构的视频生成模型参数量大、去噪步骤多，计算开销过高，难以在端侧高效部署。

### 方法关键点
1. 采用蒸馏引导的剪枝方法得到轻量模型，保留电影级效果所需的核心生成能力；
2. 结合扩散蒸馏和强化学习，将压缩后的模型优化为4步生成器，大幅降低迭代开销；
3. 采用混合训练后量化策略，把模型体量压缩到1GB以内。

### 关键结果
对比Wan 2.1架构教师模型，生成速度提升40倍，视觉效果相当；在联发科天玑8400平台上生成49帧480p视频仅需20s，峰值内存占用1.8GB，NVIDIA H200上单步去噪时延仅0.6s
