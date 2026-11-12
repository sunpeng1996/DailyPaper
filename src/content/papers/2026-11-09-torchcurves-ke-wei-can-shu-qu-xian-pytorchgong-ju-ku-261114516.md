---
title: 'TorchCurves: Differentiable Parametric Curves'
title_zh: TorchCurves：可微参数曲线PyTorch工具库
authors:
- Alex Shtoff
arxiv_id: '2611.14516'
url: https://arxiv.org/abs/2611.14516
pdf_url: https://arxiv.org/pdf/2611.14516
published: '2026-11-09'
collected: '2026-11-12'
category: Other
direction: 可微参数曲线 · PyTorch工具库
tags:
- PyTorch
- B-spline
- Legendre polynomial
- KAN
- parametric curve
one_liner: 开源PyTorch可微参数曲线库，支持B样条、勒让德基，可嵌入KAN等模型联合训练
practical_value: '- 可复用该库实现连续特征的可微embedding，替代推荐场景中离散分桶的数值特征处理，减少信息损失

  - 可基于该库快速搭建可训练KAN模型，用于CTR预估、用户行为序列建模等任务的特征交叉模块

  - 库的纯PyTorch向量化实现无需自定义算子，可直接嵌入现有推荐训练pipeline，降低迁移成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有机器学习场景中参数曲线（如样条、KAN基函数）无统一可学习抽象接口，各场景需重复定制实现，适配PyTorch训练生态的通用工具缺失。
### 方法关键点
1. 封装B-spline、Legendre多项式两种基的参数曲线为可学习原语，支持输入、曲线系数的双向自动求导，系数可随主模型联合优化也可由其他网络生成；
2. 提供模块化组件、函数式接口两种调用方式，纯PyTorch向量化实现无自定义硬件kernel，易读易维护。
### 关键结果
曲线计算速度优于NumPy、SciPy原生实现；KAN训练性能在中小规模任务上与EfficientKAN相当，仅在超大规模任务上存在小幅overhead。
