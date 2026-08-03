---
title: Scaling Properties of Text Conditioning in Visual Generation
title_zh: 视觉生成任务中文本条件的缩放特性研究
authors:
- Zilong Chen
- Chaorui Deng
- Kunchang Li
- Hongyi Yuan
- Haoqi Fan
affiliations:
- ByteDance Seed
arxiv_id: '2607.29679'
url: https://arxiv.org/abs/2607.29679
pdf_url: https://arxiv.org/pdf/2607.29679
published: '2026-07-30'
collected: '2026-08-03'
category: Multimodal
direction: 多模态生成 · 文生图prompt优化
tags:
- Text-to-Image
- Diffusion Model
- Prompt Engineering
- Scaling Law
- Multimodal Generation
one_liner: 发现文生图扩散损失与prompt结构化信息量正相关，依此优化的模型性能超过多数主流开源闭源模型
practical_value: '- 电商商品图生成场景可复用结构化prompt构造思路，加入商品语义、几何属性标注提升生成一致性，减少幻觉

  - 推荐系统多模态内容生成（如商品海报、短视频配图）可参考GPG/ED量化指标，避免盲目增加prompt长度导致性能下降

  - 可复用验证门控的on-policy蒸馏方法优化prompt生成器，降低文生图类AI Agent的冷启动成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文生图扩散模型的文本条件缩放规律缺乏定量研究，单纯增加prompt token数反而会降低生成性能，无法有效利用文本输入提升生成质量。
### 方法关键点
提出两个互补的结构化信息量量化指标：白盒似然指标GPG、黑盒属性指标ED，验证收敛扩散损失随GPG线性下降、随ED服从幂律分布下降；基于缩放规律，通过添加图像语义+几何标注构造结构化prompt提升diffusability，通过有监督微调+冷启动+验证门控on-policy蒸馏训练prompt生成器提升promptability。
### 关键结果
优化后的系统在几乎所有组合性、推理、世界知识基准上超过所有参评开源模型，多数指标匹配或超越当前最强闭源模型。
