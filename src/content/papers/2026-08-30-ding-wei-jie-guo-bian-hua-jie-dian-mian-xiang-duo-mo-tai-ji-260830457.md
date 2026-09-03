---
title: Learning Where Outcomes Change:Credit-Addressable Reasoning for Multimodal
  Geometry
title_zh: 定位结果变化节点：面向多模态几何推理的信用可寻址推理框架
authors:
- Jiani Guo
- Junjie Wang
- Jie Wu
- Pengxiang Zhao
- Dongdong Zhang
- Shaohan Huang
- Yujiu Yang
- Furu Wei
affiliations:
- Tsinghua University
- Microsoft Research
- Zhejiang University
arxiv_id: '2608.30457'
url: https://arxiv.org/abs/2608.30457
pdf_url: https://arxiv.org/pdf/2608.30457
published: '2026-08-30'
collected: '2026-09-03'
category: Reasoning
direction: 多模态推理 · 强化学习信用分配
tags:
- Multimodal Reasoning
- VLM
- GRPO
- Chain-of-Thought
- Credit Assignment
one_liner: 提出信用可寻址推理范式及Code-CoT、CE-GRPO方法，解决多模态长链推理的信用分配问题
practical_value: '- 长链多模态任务（如电商图文理解、Agent多步决策）可复用CE-GRPO的局部信用分配逻辑，替代全轨迹GRPO解决长路径下的信用弥散问题，提升优化效率

  - 结构化推理链设计可参考Code-CoT思路，将推理步骤拆分为可寻址语义单元，可用于推荐系统用户需求拆解、多步召回逻辑的错误定位与可解释性优化

  - 推理表示与优化算法协同设计的思路可迁移至强依赖多步任务（如复杂query搜索意图理解、广告文案生成效果归因），提升长序列任务性能'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：多模态几何推理要求VLMs精准提取视觉关系并完成多步推导，现有自由形式推理链无法定位关键决策点，全轨迹强化学习仅能传递终端反馈，存在严重信用弥散问题，无法单独评估每个决策的影响。

**方法关键点**：1. 提出信用可寻址推理范式，将推理过程中的显式语义单元作为信用分配的锚点；2. 设计Code-CoT，将视觉关系表示为行级可寻址的可执行代码，把推理过程组织为带类型的事件单元；3. 提出CE-GRPO，通过结构先验与类型归一化熵划分事件边界，从共享前缀采样完整后续路径，将结果差异转化为局部优势信号完成精准优化。

**关键结果**：在9个几何基准数据集上平均准确率达76.04，较Qwen3-VL-8B、轨迹级GRPO分别提升8.09、3.43个百分点，相对优势随中间事件数量增加而提升。
