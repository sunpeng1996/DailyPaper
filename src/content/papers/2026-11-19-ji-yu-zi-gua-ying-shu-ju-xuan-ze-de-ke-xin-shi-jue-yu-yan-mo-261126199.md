---
title: Learning to Think with Images Faithfully via Adaptive Data Selection
title_zh: 基于自适应数据选择的可信视觉语言模型图像推理方法
authors:
- Yu Zhao
- Jiaxin Zhang
- Rohit Saxena
- Fazl Barez
- Pasquale Minervini
- Yiwen Guo
affiliations:
- University of Edinburgh
- LIGHTSPEED
- University of Oxford
- Miniml.AI
- Independent Researcher
arxiv_id: '2611.26199'
url: https://arxiv.org/abs/2611.26199
pdf_url: https://arxiv.org/pdf/2611.26199
published: '2026-11-19'
collected: '2026-11-20'
category: Multimodal
direction: 多模态推理 · 工具调用可信度优化
tags:
- VLM
- Tool Use
- Faithfulness
- Multimodal Reasoning
- Data Selection
one_liner: 通过自适应数据选择与奖励机制提升视觉语言模型图像推理的可信度与性能
practical_value: '- 多模态商品搜索场景可复用小物体定位+细粒度问题合成pipeline，生成训练数据提升商品细节识别准确率

  - 工具调用型Agent训练时，可借鉴自适应数据选择思路，动态筛选仅靠工具输出才能正确回答的样本，减少无效工具调用幻觉

  - 工具类Agent的奖励函数可加入自适应判断项，无必要时惩罚工具调用、直接输出结果，平衡推理效率与可信度'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有Thinking with Images（TwI）类VLM虽推理准确率高，但工具调用不可信，常调用缩放工具却不依赖返回的裁剪区域结果，根源是训练数据包含大量无需缩放即可回答的样本，模型训练过程中逐渐学会跳过工具直接答题，放大了幻觉问题。
### 方法关键点
1. 设计适配模型迭代能力的动态数据选择机制，仅保留缩放后证据能有效辅助答题的样本训练；
2. 配套小物体定位+细粒度可验证问题的数据合成pipeline，扩充有效训练数据；
3. 加入自适应奖励，无缩放必要时鼓励模型直接答题，避免冗余工具调用。
### 关键结果
在视觉搜索基准V*上准确率提升11.6%，HR-Bench 4K提升7.9%，HR-Bench 8K提升9.4%，多模态幻觉指标优于所有TwI基线，且提升可信度的同时未损失推理准确率。
