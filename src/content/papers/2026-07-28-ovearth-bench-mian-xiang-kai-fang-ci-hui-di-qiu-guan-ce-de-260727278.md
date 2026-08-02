---
title: 'OVEarth-Bench: Evaluating Category Breadth and Query Diversity for Open-Vocabulary
  Earth Observation'
title_zh: OVEarth-Bench：面向开放词汇地球观测的类别覆盖与查询多样性评测基准
authors:
- Kaiyu Li
- Zepeng Xin
- Zixuan Jiang
- Jing Fu
- Lanxuan Xue
- Lingyu Zhang
- Xiangyong Cao
affiliations:
- Xi'an Jiaotong University
arxiv_id: '2607.27278'
url: https://arxiv.org/abs/2607.27278
pdf_url: https://arxiv.org/pdf/2607.27278
published: '2026-07-28'
collected: '2026-08-02'
category: Eval
direction: 开放词汇感知 · 评测基准构建与模型对比
tags:
- Benchmark
- Open-Vocabulary
- MLLM
- Zero-Shot
- Evaluation
- Multimodal
one_liner: 推出覆盖广层级类别、多类型查询的开放词汇地球观测零样本评测基准OVEarth-Bench
practical_value: '- 垂域（如电商商品、本地生活POI）开放词汇检索/定位评测集构建，可复用「层级化类别覆盖+多类型查询设计」的框架，降低评测偏差

  - 垂域多模态搜索选型可参考结论：通用MLLM零样本效果普遍优于仅在小批量垂域数据微调的专用模型，可降低冷启动成本

  - 多模态召回/定位任务的评测体系设计，可同时支持不同粒度的匹配指标（如商品局部/整体匹配、POI边界/坐标匹配），评估更全面'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有开放词汇地球观测（EO）评测基准普遍存在类别覆盖范围窄、查询形式单一的缺陷，无法全面评估模型零样本定位任意自然语言描述地理空间概念的能力，评测结果偏差大。
### 方法关键点
推出OVEarth-Bench评测基准，从两个维度升级现有评测体系：1）类别广度：覆盖层级化全量EO类别，同时包含正、负语义表达，覆盖长尾细粒度概念；2）查询多样性：支持词汇类、指代类、推理类三类用户查询，在统一Zero-Shot协议下同时支持掩码、边界框两种定位任务评测。
### 关键结果
对十余款通用与EO专用模型的评测显示：①当前开放词汇EO模型整体性能仍有较大提升空间，更广的类别覆盖可输出更稳定的模型能力排序；②MLLM类方法整体性能最优；③EO专用方法效果普遍弱于通用大模型，极少能追平SOTA通用模型。
