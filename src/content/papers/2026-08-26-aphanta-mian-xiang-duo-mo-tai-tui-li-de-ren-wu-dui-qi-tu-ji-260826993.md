---
title: 'Aphanta: Diagnosing Task-Aligned Image-Edited Intermediates for Multimodal
  Reasoning'
title_zh: Aphanta：面向多模态推理的任务对齐图像编辑中间件诊断框架
authors:
- Hengyuan Xu
- Wei Cheng
- Yumeng Ji
- Xuanyang Zhang
- Xianfang Zeng
- Gang Yu
- Xingjun Ma
affiliations:
- Fudan University
- StepFun
- Shanghai Jiao Tong University
arxiv_id: '2608.26993'
url: https://arxiv.org/abs/2608.26993
pdf_url: https://arxiv.org/pdf/2608.26993
published: '2026-08-26'
collected: '2026-08-28'
category: Eval
direction: 多模态推理 · 图像编辑工具效用诊断
tags:
- Multimodal Reasoning
- MLLM
- Image Editing
- Tool Use
- Evaluation Framework
one_liner: 提出Aphanta闭环诊断框架，量化不同任务下图像编辑中间件对MLLM推理的效用边界
practical_value: '- 多模态Agent做工具调用决策时，可参考任务分层结论，仅在grounding、局部提示注入、反事实状态生成三类场景调用图像编辑工具，避免在符号/拓扑敏感的结构化推理场景调用，减少无效算力开销

  - 评估带图像工具的多模态pipeline时，可复用三条件对照法，区分工具实现gap与任务本身的视觉增益空间，精准定位优化方向

  - 电商场景的商品瑕疵检测、遮挡商品还原、属性标注等任务，可直接复用正样本任务pipeline，通过编辑高亮/补全遮挡的方式提升MLLM识别准确率

  - 做工具调用相关LoRA微调时，可参考任务分层采样策略，对高增益任务做样本上采样，平衡训练资源投入与收益'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前MLLM常调用图像编辑工具生成中间视觉状态辅助推理，但现有方案默认编辑后的图像对所有任务都有效，未区分任务本身的增益空间与编辑器的实现缺陷，也缺乏统一框架量化不同任务下的实际效用，导致大量场景调用图像编辑工具反而降低推理准确率、增加算力开销。

### 方法关键点
- 三条件对照诊断协议：分别测试直接推理（A）、调用编辑器生成中间图推理（B）、用理想构造的参考中间图推理（C）三个组的得分，通过Δedit=SB-SA量化实际工具增益，Δref=SC-SA量化任务的理论视觉增益空间，二者差值即为编辑器的实现gap
- 四阶段自动化任务发现pipeline：包含任务提案筛选、初步诊断、数据构造、训练评估四个环节，完整保留失败/低增益任务，避免仅报告正样本带来的偏差
- 覆盖20类多模态推理任务，包含grounding、提示注入、反事实状态生成、结构化extrapolation四大类，构建Aphanta Train/Test数据集

### 关键实验
跨20个任务测试多个MLLM+编辑器组合，反事实状态生成类任务平均Δedit达+0.297，提示注入类+0.170，grounding类+0.100，而结构化推理类Δedit为-0.069，反而降低性能；整合训练的Qwen+Qwen-Image-Edit pipeline在正样本任务子集上得分从0.343提升到0.445，绝对提升10.2个百分点，相对提升29.7%，仍存在0.113的编辑器实现gap（参考得分0.558）。

### 核心结论
图像编辑是专用的视觉工作空间，而非通用的推理机制，仅在任务、中间表示、编辑器三者对齐时才能带来增益。
