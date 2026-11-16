---
title: 'MMFlash: Faster Speculative Decoding for Vision-Language Models'
title_zh: MMFlash：面向视觉语言模型的快速无损推测解码框架
authors:
- Sicheng Feng
- Zigeng Chen
- Song Wang
- Gongfan Fang
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2611.18482'
url: https://arxiv.org/abs/2611.18482
pdf_url: https://arxiv.org/pdf/2611.18482
published: '2026-11-12'
collected: '2026-11-16'
category: LLM
direction: VLM推理加速 · 扩散式推测解码
tags:
- Speculative Decoding
- Vision-Language Model
- Diffusion Drafter
- Inference Acceleration
- Sparse Attention
one_liner: 提出视觉感知损失重加权与长视频稀疏注意力，实现VLM最高3.58倍无损推理加速
practical_value: '- 多模态Agent、商品图文/短视频理解业务可直接复用MMFlash方案，将VLM推理速度提升2~3倍，相同GPU算力下请求承载量翻倍，降低推理成本

  - 多模态小模型对齐大模型时，可复用视觉依赖度加权损失设计：离线预计算每个token对视觉输入的KL依赖分，对高依赖、预测错误的token加权重，大幅提升难例拟合效率，无需盲目堆训练数据

  - 长视频/长图文多模态任务（如电商短视频理解、商品详情页OCR解析）可复用稀疏注意力设计：保留少量sink token、步长采样视觉token、全量保留文本token，将40K+长度上下文压缩到1.6K，推理速度提升20%以上不损失效果

  - 高并发多模态服务场景（如搜索query多模态理解、商品图实时审核）可参考动态块大小调度策略，根据实时并发调整diffusion块大小，平衡延迟和吞吐量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有文本场景的扩散式推测解码（如DFlash）直接迁移到VLM时性能掉点严重，核心原因是高度依赖视觉输入的token接受率仅22%，为低视觉依赖token的一半，仅用多模态数据训练无法缩小该差距，导致VLM推理速度受限于自回归生成，高并发场景下成本过高。

### 方法关键点
- 提出token级视觉依赖度指标：用目标VLM在带/不带视觉输入下的next-token分布KL散度量化每个token的视觉依赖程度，可离线预计算无额外训练成本
- 设计视觉感知损失重加权机制：损失权重结合三要素：位置生存概率（越靠后的token被验证到的概率越低，权重越低）、视觉依赖分（越高权重越高）、当前模型预测错误概率（预测越错权重越高，拟合后自动降权避免过拟合）
- 长视频场景引入稀疏注意力模式：仅保留4个sink token、步长32采样视觉token、全量文本token、256大小的局部窗口，把40K+上下文压缩到约1.6K，训练推理共用同一模式保证效果一致

### 关键实验
实验覆盖7个图像多模态基准（ChartQA、MMStar等）、3个长视频基准，对比MTP、EAGLE-3、DFlash等主流方案，基于Qwen3.5 4B/9B、Gemma4 4B、Qwen3.8 27B验证：贪心解码下平均加速3.00~3.05×，最高3.58×，比DFlash高10.3~10.9%，比EAGLE-3高195.4%；长视频场景平均加速2.33~2.71×，比DFlash高11.2~23.2%；并发32时仍有1.35×以上加速，16并发时吞吐量比基线32并发更高。

### 最值得记住的一句话
多模态小模型对齐大模型时，优先给高输入依赖的难例分配训练权重，比盲目增加训练数据、扩大模型规模的效率高得多。
