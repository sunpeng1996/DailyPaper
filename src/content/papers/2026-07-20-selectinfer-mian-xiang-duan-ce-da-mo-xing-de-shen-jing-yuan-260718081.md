---
title: 'SelectInfer: Selective Neuron Loading and Computation for On-Device LLMs'
title_zh: SelectInfer：面向端侧大模型的神经元级加载与推理优化框架
authors:
- Huzaifa Shaaban Kabakibo
- Eric Schniedermeyer
- Artem Burchanow
- Lin Wang
affiliations:
- Paderborn University, Germany
arxiv_id: '2607.18081'
url: https://arxiv.org/abs/2607.18081
pdf_url: https://arxiv.org/pdf/2607.18081
published: '2026-07-20'
collected: '2026-07-21'
category: LLM
direction: 端侧LLM · 推理加速优化
tags:
- On-device-LLM
- Inference-Optimization
- Neuron-Sparsity
- Edge-Deployment
- Selective-Inference
one_liner: 通过离线识别通用与任务专属神经元，结合选择性加载与计算，实现端侧LLM推理的内存速度精度三方均衡
practical_value: '- 端侧电商/推荐Agent部署可复用神经元分群思路：离线标注业务场景（如商品QA、文案生成）的专属神经元与通用神经元，无需全量加载模型即可适配商家终端、线下智能设备等内存受限场景

  - 低延迟场景可复用选择性计算trick：固定加载业务高频静态神经元（如商品属性理解相关），动态神经元根据用户实时请求prefill阶段激活度选择，可在几乎无损效果前提下提升推理速度

  - 低精度kernel支持差的端侧设备可替代4-bit量化方案：SelectInfer保留全精度参数，推理速度比4-bit量化高1.5~2倍，无需适配量化精度损失，适合对准确率要求高的端侧业务'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
端侧LLM部署需求随隐私保护、低延迟响应、离线可用要求提升快速增长，但现有优化方案均存在短板：量化可降低内存但会损失解码吞吐、剪枝需要成本极高的重训、运行时稀疏方案仍要求全量模型加载到内存，无法同时平衡内存占用、推理速度、输出精度三个端侧部署的核心约束。

### 方法关键点
- 离线profiling阶段：统计Transformer FFN层神经元的激活规律，将其分为两类——通用型神经元跨任务稳定激活，任务专属神经元仅在特定任务下高频激活，输出按重要度排序的神经元索引文件
- 选择性加载：根据设备内存上限，优先加载任务专属base神经元，再补充通用secondary神经元，仅加载指定比例的FFN神经元，其余参数直接丢弃，降低内存占用
- 选择性计算：运行时将已加载神经元拆分为静态（全量计算的任务专属神经元）和动态（prefill阶段按输入激活度筛选的Top神经元），仅计算40%左右的神经元，降低计算开销

### 关键实验
在8G共享内存的NVIDIA Jetson Orin Nano设备上测试Llama3.2-1B/3B、Qwen2.5-3B三个模型，覆盖QA、翻译、摘要三类任务，对比CoreInfer、4-bit量化、磁盘offloading三个基线：
- 内存：3B级模型比原生全量加载省13%左右内存，可在Jetson上正常运行原本放不下的3B模型
- 速度：Llama3.2-3B推理速度达9.85 tokens/s，是4-bit量化的1.53倍，是磁盘offloading的13倍以上
- 精度：仅加载70%神经元时，多数任务精度与4-bit量化相当，翻译任务精度显著优于量化方案

### 核心结论
端侧LLM优化不需要一刀切做压缩，通过离线先验识别神经元的任务属性，可实现内存、速度、精度的细粒度可调平衡。
