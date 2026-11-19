---
title: 'Out of Sight, Still in Mind: Token Compression for Omni-LLMs'
title_zh: ReMo：全模态大模型免训练跨模态Token压缩方法
authors:
- Suho Yoo
- Youngjoon Jang
- Hyebin Cho
- Joon Son Chung
affiliations:
- KAIST
- University of Oxford (VGG)
arxiv_id: '2607.21179'
url: https://arxiv.org/abs/2607.21179
pdf_url: https://arxiv.org/pdf/2607.21179
published: '2026-11-16'
collected: '2026-11-19'
category: LLM
direction: 全模态大模型 · 推理加速 Token压缩
tags:
- Omni-LLM
- Token Compression
- Training-Free
- Cross-Modal Alignment
- Inference Acceleration
one_liner: 提出免训练跨模态Token压缩框架ReMo，压缩54%输入Token精度反超全Token基线
practical_value: '- 电商多模态导购Agent/生成式推荐场景可直接复用ReMo的视觉Token压缩逻辑，降低KV cache占用，减少长会话、多商品展示场景的推理延迟与成本

  - 短视频/直播商品打标、多模态内容理解场景，可借鉴轻量检测器输出文本代理替换冗余视觉Token的思路，在无损理解精度的前提下压缩30%以上推理成本

  - 跨模态特征对齐无需额外微调，闭源CCA校准投影的方法可直接复用，避免为对齐音视频特征定制微调任务，大幅降低落地成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Omni-LLM同时处理音、视、文本多模态输入时，视觉Token占输入总量90%以上，是推理延迟与内存占用的核心瓶颈；现有Token压缩方案要么需针对每个模型backbone单独微调适配，要么跨模态冗余识别不准确、额外引入大体积外部模块，落地成本极高。

### 方法关键点
- 跨模态对齐投影：基于少量配对音视频数据预计算闭源CCA校准矩阵，将音视频embedding投影到公共空间，精准识别被音频或其他视觉Token覆盖的冗余视觉Token并删除
- 语义转存文本代理：用轻量YOLO检测器识别视觉物体，将物体名称+空间位置编码为带TMRoPE位置编码的文本代理插入输入序列，替代被删除视觉Token携带的语义信息
- 细节恢复与时序合并：额外恢复局部差异大的视觉细节Token，合并相邻时间块的同位置相似视觉Token，进一步压缩冗余同时保留关键信息

### 关键实验
在Qwen2.5-Omni 3B/7B、Qwen3-Omni 30B三个规模模型上验证，对比FastV、OmniZip等7种SOTA免训练压缩基线；压缩54%输入Token的前提下，平均精度达全Token模型的101.2%（3B）、101.4%（7B）、100.7%（30B），推理latency降低约40%，GPU内存占用降低约22%；极端压缩90%Token时精度下降幅度仍远低于所有基线。

### 最值得记住的一句话
多模态Token压缩的核心不是删除信息，而是将冗余信息转存到更低成本的模态表达中，用最少的Token量保留完整语义
