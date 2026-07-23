---
title: 'Subliminal Clocks: Latent Time Modelling in Diffusion Language Models'
title_zh: 潜态时钟：扩散语言模型中的隐式时间建模
authors:
- Maximo Eduardo Rulli
- Thomas Vaitses Fontanari
- Simone Petruzzi
- Federico Alvetreti
- Giorgio Strano
- Donato Crisostomi
- Giorgos Nikolaou
- Tommaso Mencattini
- Andrea Santilli
- Emanuele Rodolà
affiliations:
- Sapienza University of Rome
- EPFL
- NVIDIA
arxiv_id: '2607.01774'
url: https://arxiv.org/abs/2607.01774
pdf_url: https://arxiv.org/pdf/2607.01774
published: '2026-07-19'
collected: '2026-07-23'
category: LLM
direction: 扩散语言模型 · 隐式表征机制研究
tags:
- Diffusion Language Model
- DLM
- Latent Representation
- Activation Probing
- Generation Steering
one_liner: 发现扩散语言模型内部隐式编码扩散时间步信息，可提取并调控生成置信度与熵
practical_value: '- 基于DLM生成电商文案/推荐话术时，可提取隐式时间步信号判断生成进度，提前终止低质量生成，降低推理成本

  - 调控DLM的时间步相关低维子空间，可按需调整生成结果置信度，适配不同场景（商品描述要低熵确定，营销文案要高熵多样）

  - 内部激活探针方法可复用在大模型推荐系统的黑盒解释上，定位生成推荐结果的关键表征层'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
Diffusion Language Models (DLMs) 作为自回归LLM的新兴替代方案，未显式输入扩散时间步，其内部是否编码去噪进度、该信息如何影响下游生成的机制尚不清晰。
### 方法关键点
1. 跨层部署线性探针提取DLM残差流的内部激活，验证扩散时间步相关隐表征的存在性；
2. 沿时间步关联的低维子空间对模型进行steer操作，观测生成行为的变化规律；
3. 分析该隐表征在激活空间的几何特性，解释其处理逻辑。
### 关键结果
- 跨层探针可稳定解码DLM的隐式去噪进度信号，解码准确率远高于随机水平；
- 调控时间步子空间可系统性调整生成结果的置信度与熵，变化趋势完全可预测；
- 时间步表征在激活空间具备连续、结构化的可解释几何属性。
