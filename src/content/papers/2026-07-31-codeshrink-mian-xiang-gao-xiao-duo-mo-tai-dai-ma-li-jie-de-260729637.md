---
title: 'CodeShrink: Adaptive Visual Compression for Efficient Multimodal Code Understanding'
title_zh: CodeShrink：面向高效多模态代码理解的自适应视觉压缩框架
authors:
- Wenxin Tang
- Jingyu Xiao
- Zhenyu Liu
- Zipeng Xie
- Junliang Liu
- Wang Luo
- Yuan Jiang
- Yintong Huo
- Michael Lyu
affiliations:
- 清华大学
- 香港中文大学
- 西北工业大学
- 西安交通大学
- 中山大学
arxiv_id: '2607.29637'
url: https://arxiv.org/abs/2607.29637
pdf_url: https://arxiv.org/pdf/2607.29637
published: '2026-07-31'
collected: '2026-08-04'
category: Multimodal
direction: 多模态大模型 · 输入Token压缩
tags:
- MLLM
- Token Compression
- Multimodal Understanding
- Reinforcement Learning
- Code Intelligence
one_liner: 提出面向多模态代码理解的自适应视觉压缩框架，视觉token减少71.2%同时性能不降反升
practical_value: '- 多模态Agent处理商品详情、商家长文案等结构化内容时，可借鉴无空白渲染思路，先剔除无效空白、冗余布局元素，大幅降低视觉token开销

  - 可复用自适应压缩配置的轻量RL Agent思路，针对不同用户query、内容类型动态调整压缩策略，平衡推理效率和内容保真度

  - 生成式推荐、多模态搜索场景可借鉴指令感知的token剪枝逻辑，仅保留与用户需求相关的视觉/文本token，降低大模型推理成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态大模型（MLLM）处理代码类结构化视觉输入时，仅靠分辨率缩放压缩效率低下：既忽略换行、缩进带来的大量空白区域，也未剪去与当前指令无关的冗余内容，且固定压缩比策略无法适配不同输入、任务、模型的差异化需求。
### 方法关键点
CodeShrink包含三个核心模块：
1. 无空白渲染：用紧凑布局+显式结构标记替换依赖空白的排版，消除布局带来的冗余token
2. 自适应压缩配置：用RL训练的轻量Agent逐输入预测压缩参数，平衡token效率与内容可读性
3. 主导token选择：联合分析指令与输入图像，推理时直接剪去任务无关的视觉token
### 关键结果
在代码问答、克隆检测、代码补全三类任务上，视觉token用量最高降低71.2%，性能持平甚至超过未压缩的纯文本输入，全面优于各类文本、视觉压缩基线。
