---
title: Language Models Can Rewrite Their Own Weights
title_zh: 大语言模型可自主改写自身权重
authors:
- Jiajun Fan
- Neil He
- Changyi Yang
- Andy Mao
- Xi Zhu
- Chaoran Cheng
- Kaiqu Liang
- Shuaike Shen
- Zetian Li
- Ruihan Guo
affiliations:
- UIUC
- CMU
- Rutgers
- Princeton
- Stanford
arxiv_id: '2611.21885'
url: https://arxiv.org/abs/2611.21885
pdf_url: https://arxiv.org/pdf/2611.21885
published: '2026-11-15'
collected: '2026-11-21'
category: LLM
direction: 大模型自优化 · 无梯度权重改写
tags:
- LLM
- self-rewriting
- weight-editing
- self-improvement
- no-gradient
one_liner: 首次实现无梯度无训练的大模型自主权重改写，27B模型可自我优化与修复
practical_value: '- 可借鉴「错误样本hidden state差异定位→轻量权重修改→小流量验证保留有效改动」的迭代框架，替代部分小版本重训练需求，降低垂直领域LoRA模型的迭代成本

  - 针对业务场景中常见的LLM重复生成、输出截断、bad case集中等问题，无需重新训练，通过极小幅度的秩一权重修改即可定向修复

  - 自我修复逻辑可复用至线上LLM服务故障自愈：自动定位权重漂移/硬件故障导致的异常权重块，无需切流回滚即可快速恢复服务可用性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM训练完成后即冻结，优化要么依赖重训练需要大量算力与基建投入，要么通过prompt、测试时优化获得的收益无持久性，训练与推理的严格边界不符合类人智能边用边进化的特性，亟需探索低代价的模型持续优化路径。
### 方法关键点
- 给模型开放自身权重读写、前向推理测试、hidden state读取权限，全程禁止梯度计算与优化器调用，仅通过模型自主推理完成权重修改
- 自我优化流程：基于错误样本诊断问题，对比正常/异常输出样本的hidden state定位问题层与差异方向，仅做极小幅度的秩一修改/异常值截断，通过配对同种子测试验证改动收益后才保留
- 自我修复流程：仅告知模型存在权重损坏，由模型自主遍历权重矩阵定位异常值，通过截断异常权重完成修复
### 关键结果
测试基于Qwen3.5 2B/4B/9B/27B同系列模型，仅27B具备自改写能力：自我优化后在490个未见过的数学题上准确率提升6.6个百分点，输出截断率降低7.5个百分点；自我修复任务中，仅损坏1层MLP输出矩阵的模型从0准确率恢复到文本任务33%准确率、6个未见过的图像任务70.2%准确率，达到原模型83%的性能。
### 最值得记住的话
训练和推理的边界是现有工具的限制，而非智能本身的属性。
