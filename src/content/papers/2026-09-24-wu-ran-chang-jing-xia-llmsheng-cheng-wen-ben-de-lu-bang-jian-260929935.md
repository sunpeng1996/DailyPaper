---
title: Robust Detection of LLM-Generated Text under Contamination
title_zh: 污染场景下LLM生成文本的鲁棒检测
authors:
- Jiaxun Li
- Saptarshi Chakraborty
- Ambuj Tewari
affiliations:
- Department of Statistics, University of Michigan
arxiv_id: '2609.29935'
url: https://arxiv.org/abs/2609.29935
pdf_url: https://arxiv.org/pdf/2609.29935
published: '2026-09-24'
collected: '2026-09-26'
category: LLM
direction: LLM生成内容检测 · 鲁棒性优化
tags:
- LLM Generated Text
- Robustness
- Contamination
- Statistical Test
- Clipping
one_liner: 通过给统计检测器加clipping修正提升污染场景下LLM生成文本检测的鲁棒性
practical_value: '- 电商内容风控场景下，可直接给现有LLM生成文本统计检测器加clipping修正，无需重新训练即可提升AI生成文案加人工修改这类污染场景的识别准确率

  - 参考文中Huber污染建模思路，对风控规则的异常得分做截断处理，降低恶意篡改样本对检测效果的负面影响

  - UGC/AI生成商品文案合规校验场景可直接采用clipped LRR检测器，5%误报率下真阳率最高可提升8.3个百分点'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有LLM生成文本检测器仅在干净样本上效果好，遇到人工编辑、人机内容混杂的污染场景时性能大幅衰减，缺乏明确的检测可行性边界和低成本鲁棒优化方案。

### 方法关键点
将人类/LLM生成文本建模为带Huber污染的有限阶马尔可夫过程，推导得到可靠检测的精确边界：污染程度超过干净源区分度阈值时检测完全不可行，低于阈值时采用clipped似然比检验可将最坏误差降至0；提出给现有统计检测器的加性得分加clipping的轻量改造方案，无需重构检测器。

### 关键结果数字
在3个数据集、3个生成模型、RAID基准上测试7种检测器，clipping可稳定提升鲁棒性：5%目标误报率下，LRR检测器真阳率在受控实验中位提升8.3个百分点，RAID基准的速率/攻击专项测试中分别提升2.1、4.3个百分点。
