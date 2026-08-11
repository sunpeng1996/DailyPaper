---
title: 'Sci-VBench: Evaluating Knowledge- and Reasoning-Intensive Video Generation
  in Science Domains'
title_zh: Sci-VBench：科学领域知识与推理密集型视频生成评估基准
authors:
- Diandian Zhang
- Tingyu Song
- Lin Fu
- Zheyuan Yang
- Yilun Zhao
affiliations:
- Zhejiang University
- UCAS
- Tongji University
- Yale University
arxiv_id: '2608.09873'
url: https://arxiv.org/abs/2608.09873
pdf_url: https://arxiv.org/pdf/2608.09873
published: '2026-08-09'
collected: '2026-08-11'
category: Eval
direction: 评估基准 · 科学域视频生成
tags:
- Evaluation Benchmark
- Video Generation
- MLLM-as-Judge
- Knowledge Reasoning
- Causal Correctness
one_liner: 构建科学领域知识推理密集型视频生成基准Sci-VBench，配套评估协议并测试16款主流模型
practical_value: '- 做电商商品演示、教育类带货等垂域短视频生成的评估时，可借鉴rubric-based MLLM-as-Judge评估协议，降低专业标注人力成本

  - 评估生成内容质量时，不能仅聚焦视觉观感，需拆分Prompt对齐度、事实/因果正确性等维度，避免出现看似逼真但常识错误的内容

  - 垂域生成任务的标注流程可参考「专家标注小样本+非专家/MLLM规模化评估」的范式，在保证精度的前提下提升评估效率'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
现有视频生成评估多聚焦表面视觉合理性，缺乏面向知识、推理密集型垂域的系统性评估基准，无法衡量生成内容的科学正确性、因果合理性等深层指标。
## 方法关键点
1. 构建Sci-VBench基准，包含1253条专家标注样本，覆盖自然科学、医疗、人文社科、工程4大学科共60个细分领域，要求生成内容符合科学逻辑与时序规则；
2. 提出基于评分细则的标准化评估协议，支持非专家人工、MLLM-as-Judge两种评估模式。
## 关键结果数字
非专家、MLLM评估结果与专家判断一致性较高，可支撑大规模可复现评估；测试16款前沿开源/闭源模型，感知质量得分差异极小，但Prompt对齐度、科学与因果正确性得分差异显著，闭源模型性能大幅领先开源模型，当前视觉逼真度提升尚未转化为可靠的科学/因果动态建模能力。
