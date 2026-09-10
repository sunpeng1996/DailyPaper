---
title: 'Diffs vs. Whole Files: An Empirical Comparison of Iterative Edit-Based and
  Direct Generation for Flutter/Dart Code Models'
title_zh: Flutter/Dart代码模型迭代diff编辑与直接生成的实证对比
authors:
- Andrej Andrejev
affiliations:
- Independent researcher (bbidpa)
arxiv_id: '2609.05779'
url: https://arxiv.org/abs/2609.05779
pdf_url: https://arxiv.org/pdf/2609.05779
published: '2026-09-04'
collected: '2026-09-10'
category: LLM
direction: 代码大模型生成范式实证研究
tags:
- LLM
- Code Generation
- Empirical Study
- Diff Editing
- Direct Generation
one_liner: 实证对比代码大模型直接生成与迭代diff编辑范式的优劣及适用边界
practical_value: '- 开发代码类Agent（如推荐系统自动化运维、广告策略代码迭代工具）时，默认优先采用直接生成完整文件的范式，可避免diff编辑的累积错误，整体准确率更高

  - 针对小范围代码重构、边缘case修复这类局部修改需求，可切换为diff编辑范式，既节省token成本，效果也能与直接生成相当

  - 可在代码Agent前加一层任务预判模块，先评估待修改内容的局部性、预计编辑步数，动态选择最优生成范式，平衡效果与推理成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
代码编辑类LLM存在两种主流输出范式：直接生成完整修改后文件、迭代输出局部search/replace的diff编辑，后者看似符合人类编辑习惯、单轮生成token量更低，但二者的效果差异与适用边界缺乏系统实证对比。
### 方法关键点
在同一Flutter/Dart代码编辑数据集上，分别对两种架构（从零训练的100M参数Rainbow-Pony-100M、微调的Qwen2.5-Coder-0.5B）各训练两种范式的模型，在1790个测试任务上做控制变量对比，排除任务难度、编译通过率的干扰。
### 关键结果
直接生成范式在编译/静态分析通过率、字符级相似度、盲审LLM-judge的目标完成度/正确性/代码质量打分等所有指标上均显著优于diff编辑范式；仅在编辑步数极少的局部修改场景（重构、错误/边缘case修复），diff范式效果与直接生成相当。
