---
title: SepPrune:A Separator-based Pruning Framework for Efficient Multimodal Large
  Language Models
title_zh: SepPrune：基于分隔符的多模态大模型高效剪枝框架
authors:
- Yuchen Wang
- Qihui Zhu
- Yang Liu
- Xiaoyan Sun
- Siying Wu
affiliations:
- 中国科学技术大学
- 合肥综合性国家科学中心
- 长鑫存储技术有限公司
arxiv_id: '2607.25818'
url: https://arxiv.org/abs/2607.25818
pdf_url: https://arxiv.org/pdf/2607.25818
published: '2026-07-28'
collected: '2026-07-29'
category: Multimodal
direction: 多模态大模型 · 视觉Token剪枝优化
tags:
- MLLM
- Token Pruning
- Inference Acceleration
- Training-free
- Plug-and-Play
one_liner: 利用模态分隔符做统一查询实现免训练免改结构的MLLM视觉Token剪枝
practical_value: '- 电商多模态搜索/商品理解场景可直接复用SepPrune剪枝商品图视觉Token，80%剪枝率下仅掉3.7%精度，可大幅降低高分辨率商品图推理延迟，适配FlashAttention无需改模型结构

  - 多模态Agent处理多图/视频输入时，可直接集成该训练免改的剪枝方案，用模态分隔符作为统一查询的思路复杂度仅O(N)，远低于现有O(N²)方案，端到端延迟更低

  - 对含边界特殊Token的多模态/跨模态任务，可借鉴「用天然跨模态桥接Token做全局重要性打分+去除位置编码消偏」的设计思路，不需要额外训练参数即可实现轻量化冗余过滤'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
新一代MLLM（如Qwen2.5-VL、InternVL3）的视觉编码器输出Token量大幅增加，严重拖慢推理速度；现有剪枝方案要么依赖跨模态注意力打断FlashAttention计算流，要么O(N²)复杂度抵消剪枝收益，且大多依赖<[BOS_never_used_51bce0c785ca2f68081bfa7d91973934]> Token等特定结构适配性差。

### 方法关键点
- 首次发现MLLM浅层注意力在模态分隔符位置存在峰值，分隔符是跨模态交互的核心桥接节点，删除分隔符对性能的影响远大于删除等量视觉/文本Token
- 以视觉序列后的分隔符为统一Query，复用LLM第一层的K/Q投影参数计算所有视觉Token的注意力得分，复杂度仅O(N)，不需要新增参数或训练
- 计算得分时移除RoPE位置编码，消除位置偏置，保证仅基于语义重要性排序剪枝，兼容FlashAttention、KV cache等所有现有推理加速方案，完全不改动原有模型结构

### 关键结果
在Qwen2.5-VL-7B、InternVL3-8B上覆盖12个主流多模态基准（VQA、幻觉检测、OCR类任务等），对比FastV、DivPrune、CDPruner等SOTA剪枝方案：80.2%视觉Token剪枝率下，Qwen2.5-VL-7B保留96.3%的原精度，比次优方案高2.7个百分点；60.5%剪枝率下保留99%原精度，端到端延迟比未剪枝版本低22.2%，比同类剪枝方案最高低8%。

**最值得记住的一句话：** 利用模型天然存在的跨模态桥接特殊Token做全局重要性评估，是实现无训练、免改结构、高兼容的轻量化冗余过滤的高效路径
