---
title: Do learned image captioning metrics generalize? Auditing duplicated samples
  in human-judgment benchmarks
title_zh: 图像captioning学习型指标是否可泛化？人工评测基准的重复样本审计
authors:
- Xiaochen Zhang
- Jin Li
- Chunlong Xia
- Longjiang Guo
affiliations:
- 陕西师范大学人工智能与计算机科学学院
- 百度公司
arxiv_id: '2611.30488'
url: https://arxiv.org/abs/2611.30488
pdf_url: https://arxiv.org/pdf/2611.30488
published: '2026-11-22'
collected: '2026-11-25'
category: Eval
direction: 多模态生成评测 · 基准数据质量审计
tags:
- Image Captioning
- Evaluation
- Data Leakage
- Generalization
- Benchmark
one_liner: 审计三类常用图像captioning人工评测基准的样本泄露问题，给出更严谨的评测协议
practical_value: '- 电商商品图自动文案、营销素材AIGC的效果自动评测流程中，需先做训练/测试集像素级去重，避免指标虚高误导迭代

  - 自建人工标注的内容/推荐效果评测基准时，可直接复用「无测试样本泄露训练+指标拆分报告+配对检验对比」的标准化协议

  - 多模态内容排序场景下，低分劣质样本识别任务已接近饱和，优化重点可转向中高分样本的细粒度排序能力'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
学习型图像captioning指标的效果判定核心是与人工评分的相关性，但此前未验证训练-测试样本泄露对指标泛化性的影响，导致指标效果报告可能失真。
### 方法关键点
对Polaris、Nebula、Spica三类主流人工评测基准做像素级图像匹配，控制变量重训指标验证重复样本的影响，拆分Kendall's τ为低分样本检测、中高分样本排序两个独立分量，配套给出无样本泄露的标准化评测协议。
### 关键结果
Spica训练集包含2/3的Polaris测试集，重复样本可使Pearl指标相关性虚高且随训练epoch持续增长；现有基准无法稳定排序Polos、DENEB、Pearl三类主流指标，基于冻结特征的岭回归效果可比肩甚至优于三者；新协议下零样本VLM评测器在新测试集表现最优，微调评测器在旧基准表现最优。
