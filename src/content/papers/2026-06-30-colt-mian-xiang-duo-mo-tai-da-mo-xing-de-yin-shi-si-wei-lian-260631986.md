---
title: 'CoLT: Teaching Multi-Modal Models to Think with Chain of Latent Thoughts'
title_zh: CoLT：面向多模态大模型的隐式思维链推理框架
authors:
- Lianyu Hu
- Shengqian Qin
- Zeqin Liao
- Qing Guo
- Liang Wan
- Wei Feng
- Yang Liu
affiliations:
- Nanyang Technological University
- Shanghai Jiao Tong University
- NKIARI, Shenzhen
- Nankai University
- Tianjin University
arxiv_id: '2606.31986'
url: https://arxiv.org/abs/2606.31986
pdf_url: https://arxiv.org/pdf/2606.31986
published: '2026-06-30'
collected: '2026-07-01'
category: Reasoning
direction: 多模态推理 · 隐式思维链优化
tags:
- Chain-of-Thought
- Latent Reasoning
- Multimodal LLM
- Inference Acceleration
- CoT Optimization
one_liner: 通过三重监督训练多模态模型用隐式向量替代文本CoT，推理速度提升10倍以上且精度更高
practical_value: '- 多模态商品理解、直播内容审核场景可复用这套隐式CoT方案，在保留推理精度的前提下大幅降低推理延迟，提升线上服务吞吐量

  - 做Agent推理优化时，可借鉴正向+反向+内部三重监督机制，无需额外标注就能对齐隐式向量与显式推理语义，避免训练不稳定

  - 业务侧落地隐式推理时可优先选3步隐式向量的配置，达到精度与效率的最优trade-off，轻量小解码器就能满足监督需求不需要大模型

  - 对噪声多的用户输入、低质量商品图场景，隐式推理比显式文本CoT抗噪性高50%以上，可直接复用提升复杂query召回排序的鲁棒性'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
文本CoT是当前多模态大模型的主流推理范式，但需要生成数百上千的推理token，推理延迟极高，且离散文本表达会压缩潜在推理路径空间，早期步骤错误还会逐级放大；现有隐式推理方案要么仅适配纯文本LLM，要么依赖额外辅助图像标注，落地成本高且训练不稳定，无法直接复用至多模态场景。

### 方法关键点
- 用K个连续隐式向量替代冗长的离散文本CoT步骤，推理时无需生成任何文本，默认K=3达到精度与效率的最优平衡
- 引入轻量同家族小解码器做双向监督：正向模式从当前隐式向量解码下一段文本CoT，保证隐向量包含完整推理信息；反向模式将文本CoT输入解码器得到的隐状态与模型输出对齐，锚定隐空间语义
- 新增内部过渡监督，用两层MLP从当前隐向量预测下一步隐向量，保证推理步骤的逻辑连贯性
- 训练阶段联合任务损失+三重监督损失优化，推理阶段完全丢弃解码器和MLP，无额外计算开销

### 关键实验
在8个多模态推理基准（SeedBench、MMBench、ChartQA等）上测试，基于Qwen3-VL-8B基座：对比同基座文本CoT，平均精度高3.4%，端到端推理速度快10.1×，文本解码速度快22.6×；对比最优隐式推理基线SIM-CoT，平均精度高5.1%，且不需要额外标注；在图像模糊、文本拼写错误等噪声输入下，性能衰减仅为文本CoT的60%左右，鲁棒性显著提升。

**最值得记住的一句话：** 用少量结构化监督的隐式向量替代显式文本推理，是兼顾多模态大模型推理精度、速度、鲁棒性的高性价比落地方案
