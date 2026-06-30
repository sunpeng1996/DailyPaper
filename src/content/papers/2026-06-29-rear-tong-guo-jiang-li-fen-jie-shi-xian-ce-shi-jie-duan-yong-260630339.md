---
title: 'REAR: Test-time Preference Realignment through Reward Decomposition'
title_zh: REAR：通过奖励分解实现测试阶段用户偏好重对齐
authors:
- Fuxiang Zhang
- Pengcheng Wang
- Chenran Li
- Yi-Chen Li
- Yuxin Chen
- Lang Feng
- Chenfeng Xu
- Masayoshi Tomizuka
- Bo An
affiliations:
- Nanyang Technological University
- University of California, Berkeley
- Nanjing University
arxiv_id: '2606.30339'
url: https://arxiv.org/abs/2606.30339
pdf_url: https://arxiv.org/pdf/2606.30339
published: '2026-06-29'
collected: '2026-06-30'
category: LLM
direction: LLM 测试阶段偏好对齐 · 奖励分解
tags:
- Preference Alignment
- Reward Decomposition
- Test-time Scaling
- LLM Alignment
- Training-free
one_liner: 提出奖励分解的测试阶段偏好重对齐框架，将测试时缩放扩展到通用偏好对齐任务
practical_value: '- 测试阶段免训练即可适配动态个性化偏好，可用于电商推荐场景用户临时偏好调整，无需额外微调

  - 奖励分解为任务项+偏好项的思路，可复用在Agent/RAG生成结果排序，单独加权用户偏好提升匹配度

  - 可直接集成best-of-N、树搜索等现有算法，工程改造成本低，适合业务快速落地'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM偏好对齐的后训练方案需要高昂的数据标注整理成本与额外训练开销；测试时缩放(TTS)作为免训练的高效方案，此前仅能应用在数学、编码这类正确性易判断的可验证领域，无法扩展到通用偏好对齐任务，基模型往往无法充分适配用户明确给出的个性化偏好。

### 方法关键点
将偏好对齐建模为测试时重对齐问题，核心洞察是把底层奖励函数分解为**问题相关分量**和**偏好信息相关分量**两个独立部分，推导出REAR重对齐奖励，可选择性缩放两个奖励项的权重比例；REAR可表示为token级策略对数概率的线性组合，计算效率高，无需额外训练，可轻松集成到best-of-N采样、树搜索等各类现有TTS算法中。

### 关键结果
相比各类测试时基线方法，REAR在多样用户需求的偏好对齐任务上实现了更优的可扩展测试时重对齐效果，同时能够泛化到适配偏好设置的数学、视觉多类任务。
