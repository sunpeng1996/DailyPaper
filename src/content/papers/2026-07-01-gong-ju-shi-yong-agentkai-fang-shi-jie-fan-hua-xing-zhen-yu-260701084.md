---
title: Can Agents Generalize to the Open World? Unveiling the Fragility of Static
  Training in Tool Use
title_zh: 工具使用Agent开放世界泛化性诊断与扰动增强微调方法
authors:
- Song-Lin Lv
- Weiming Wu
- Rui Zhu
- Zi-Jian Cheng
- Lan-Zhe Guo
affiliations:
- Nanjing University
- National Key Laboratory for Novel Software Technology, Nanjing University
arxiv_id: '2607.01084'
url: https://arxiv.org/abs/2607.01084
pdf_url: https://arxiv.org/pdf/2607.01084
published: '2026-07-01'
collected: '2026-07-02'
category: Agent
direction: Agent 工具调用鲁棒性优化
tags:
- LLM Agent
- Tool Use
- SFT
- RL
- Robustness
- Fine-tuning
one_liner: 定义开放世界工具使用Agent场景，诊断SFT/RL训练缺陷，提出扰动增强微调提升鲁棒性
practical_value: '- 训练电商导购、查询类工具调用Agent时，可直接复用PAFT的3种扰动策略做数据增强，无需大量真实异常样本即可提升开放环境鲁棒性

  - 动态性高的工具调用场景优先选择RL范式训练，其语义接地能力优于SFT，对工具迭代、用户指令模糊的适配性更好

  - 训练Agent时加入0.3比例的扰动样本（异常反馈、不可解样本、符号扰动），可平衡正常任务性能与异常处理能力

  - 训练阶段加入不可解场景的拒绝标注，避免Agent在工具不可用时 hallucinate 结果误导用户'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前工具使用Agent在静态基准上表现优异，但真实场景中用户Query、工具集合、交互逻辑都是动态变化的，静态训练的模型泛化性差，部署后易失效，缺乏系统的鲁棒性诊断和优化方案。

### 方法关键点
- 正式定义OpenAgent场景，覆盖查询、动作、观测、域4个维度的分布偏移，搭建可控沙箱环境拆分4层诊断框架：感知、交互、推理、内化
- 明确两类训练范式的缺陷：SFT存在符号锚定依赖、轨迹惯性，RL存在目的论偏差导致的边界盲
- 提出PAFT（Perturbation-Augmented Fine-Tuning），通过3种轨迹级扰动增强训练数据：环境反馈扰动（注入异常反馈+监督修正动作）、可解性边界扰动（注入致命错误+监督拒绝动作）、符号表示扰动（改写工具名/文档强制语义接地）

### 关键结果
基于Qwen2.5-7B-Instruct，训练集6050样本，测试集880无泄露样本，对比原生SFT、RL baseline。使用PAFT后，早期SFT模型在4层测试的准确率相对闭集基准的跌幅从50%+缩小到5%以内，不可解场景拒绝率从不足1%提升到99%+，α=0.3时效果最优。

**最值得记住的一句话**：静态训练的工具Agent本质是在拟合训练分布的表层模式，而非学习泛化的工具使用逻辑，只有在训练阶段引入全链路扰动才能适配开放世界的动态性。
