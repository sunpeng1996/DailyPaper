---
title: 'WaveLLM: Wavelet-Domain LLM Entropy Modeling for Lossless Image Compression'
title_zh: WaveLLM：面向无损图像压缩的小波域大语言模型熵建模
authors:
- Yue Yu
- Bowei Kang
- Changsheng Gao
- Dong Liu
- Xiaoyan Sun
affiliations:
- University of Science and Technology of China
- Nanyang Technological University
arxiv_id: '2610.22232'
url: https://arxiv.org/abs/2610.22232
pdf_url: https://arxiv.org/pdf/2610.22232
published: '2026-10-15'
collected: '2026-10-17'
category: LLM
direction: LLM · 小波域无损图像压缩
tags:
- LLM
- Wavelet Transform
- Entropy Modeling
- Lossless Compression
- LoRA
one_liner: 提出小波域LLM熵模型WaveLLM，在多个无损图像压缩基准上实现SOTA性能
practical_value: '- 信号拆分思路可复用：将异构预测任务拆分为多组统计同构的子任务降低LLM建模难度，可迁移至多模态内容召回/排序的输入表征处理

  - 跨模态适配技巧可借鉴：针对数值型符号设计专属embedding与预测头适配LLM原生token空间，可用于推荐系统用户行为数值特征与LLM的适配

  - 单模型多任务适配方法：用任务自适应prompt实现单一共享模型适配多子任务，可复用至多场景推荐的轻量级LLM微调方案'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有LLM基无损图像压缩方案直接将图像序列化为像素/残差序列，异构信号模式在单预测流中纠缠，仅提升LLM建模容量无法突破性能瓶颈。
### 方法关键点
1. 将图像分解为多级小波子带，把异构预测问题转化为多组结构清晰、统计同构的子问题，适配自回归概率估计逻辑
2. 设计数值专属接口，通过值嵌入和系数预测头桥接数值编码符号与LLM原生文本token空间
3. 采用任务自适应prompt策略，基于Llama-3.2-3B做LoRA微调，实现单共享模型适配不同子带
### 关键结果
在Kodak、CLIC.pro、DIV2K三个基准上分别达到2.51、2.24、2.27 bpsp，较同小波变换的PixelCNN编解码器分别提升0.43、0.36、0.46 bpsp，全面优于现有SOTA LLM基无损压缩方案
