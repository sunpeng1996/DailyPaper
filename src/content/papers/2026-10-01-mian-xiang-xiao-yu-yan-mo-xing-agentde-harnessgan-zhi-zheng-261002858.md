---
title: Harness-Aware Distillation for Small Language Model Agents
title_zh: 面向小语言模型Agent的Harness感知蒸馏方法
authors:
- Moonseok Choi
- Taehong Moon
- Giung Nam
- Juho Lee
affiliations:
- KAIST AI
- Independent Researcher
arxiv_id: '2610.02858'
url: https://arxiv.org/abs/2610.02858
pdf_url: https://arxiv.org/pdf/2610.02858
published: '2026-10-01'
collected: '2026-10-07'
category: Agent
direction: Agent蒸馏 · Harness感知优化
tags:
- Agent Distillation
- On-policy Distillation
- Harness
- Small Language Model
- Preference Learning
one_liner: 设计双组件harness感知蒸馏框架，大幅提升小模型Agent蒸馏后的长horizon任务性能
practical_value: '- 电商智能导购、售后Agent等场景蒸馏小模型时，可复用HAD核心思路：不让小模型学习harness（如库存、规则、用户状态管理模块）已覆盖的能力，仅蒸馏harness无法提供的老师决策逻辑，减少冗余学习提升效果

  - 可直接复用偏好对构造方法：对同一个teacher分别输入带/不带业务系统信息（如库存、优惠规则）的prompt，构造正负动作偏好对，仅训练动作部分的偏好，避免长推理文本稀释信号

  - 零成本有效性过滤trick可直接落地：用业务系统（harness）的返回记录（如库存不足、无操作权限）过滤老师输出的错误动作，避免学生学到错误逻辑，无需额外标注

  - 梯度平衡技巧可直接复用：每次迭代动态调整蒸馏损失和偏好损失的权重，让偏好损失的梯度范数为蒸馏损失的0.5倍，避免两类损失互相干扰，无需手动调参'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent普遍基于harness（管理上下文、工具、环境反馈的外围软件）部署，大模型蒸馏为小模型时harness固定不变，传统on-policy蒸馏（OPD）无差别模仿老师全量输出，既冗余学习harness已覆盖的能力，还会把老师错误、忽略harness信息的行为传给学生，导致蒸馏后小模型harness利用率低，长horizon任务性能提升有限。

### 方法关键点
- 保留基础带harness的响应蒸馏损失，让学生模仿老师带harness时的完整输出
- 新增harness感知动作偏好学习：同个teacher分别输入带/不带harness的历史序列生成动作，训练学生在自身推理上下文下偏好带harness的动作，仅对比动作token避免推理文本稀释信号
- 新增有效性过滤：若带harness的老师动作与harness记录冲突（如使用未持有物品），则过滤该偏好对，无需额外标注即可避免学生学习错误逻辑
- 动态调整损失权重：每次迭代让偏好损失的梯度范数为蒸馏损失的0.5倍，平衡两类信号无需手动调参

### 关键实验
在ALFWorld、WebShop、ScienceWorld三个长horizon Agent基准上测试，对比4种主流on-policy蒸馏基线。蒸馏Qwen3 1.7B（从8B teacher）时，ALFWorld unseen任务成功率达63.4%，较最优基线高16.4pct，甚至超过8B教师的51.5%；harness利用率达81%，较基线高7.9pct。即便给基线2倍teacher查询预算，性能仍远低于HAD。

### 核心结论
蒸馏带固定外围系统（harness、工具、检索等）的模型时，只需聚焦系统无法覆盖的老师决策逻辑，可大幅提升蒸馏效率与效果
