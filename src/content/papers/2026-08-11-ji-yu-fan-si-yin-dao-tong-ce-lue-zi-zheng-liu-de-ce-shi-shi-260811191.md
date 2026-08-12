---
title: Test-Time Self-Evolving GUI Visual Grounding via Reflection-Guided On-Policy
  Self-Distillation
title_zh: 基于反思引导同策略自蒸馏的测试时自进化GUI视觉定位
authors:
- Shiyu Xuan
- Zechao Li
affiliations:
- School of Computer Science and Engineering, Nanjing University of Science and Technology
arxiv_id: '2608.11191'
url: https://arxiv.org/abs/2608.11191
pdf_url: https://arxiv.org/pdf/2608.11191
published: '2026-08-11'
collected: '2026-08-12'
category: Agent
direction: GUI Agent · 测试时自适应优化
tags:
- GUI-Agent
- Visual-Grounding
- Test-Time-Adaptation
- Self-Distillation
- LoRA
one_liner: 提出无需人工标注的测试时自进化GUI定位框架，通过反思引导自蒸馏实现部署后性能提升
practical_value: '- 可复用测试时自进化闭环设计：针对电商导购Agent、自动化运营Agent等部署后适配新UI的场景，无需人工标注即可通过探索-评估-反思-内化的闭环持续优化定位能力，降低冷启动成本

  - 反思引导自蒸馏的反馈转化方法：当Agent只能获取文本类反馈而非结构化标注时，可借鉴将高层推理反馈转化为token级监督信号的思路，替代传统稀疏奖励RL，提升优化效率

  - 对比校准的错误前缀抑制技巧：在自回归生成类任务（如推荐文案生成、Semantic ID生成）中，可借鉴该方法抑制错误前缀导致的监督信号污染，避免负向迁移

  - 多角色共享基座+LoRA切换的工程优化：同一基座通过切换不同LoRA适配器实现定位模型和评估反射器的角色切换，大幅降低显存占用，适合资源受限的Agent部署'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有GUI视觉定位模型部署后参数冻结，无法适配未见过的界面布局；测试时RL方法仅依赖稀疏标量奖励，无法解释失败原因、指导模型修正，难以从交互中持续进化。

### 方法关键点
- 构建探索-评估-反思-内化的闭环自进化框架，无需人工标注即可在部署后持续优化：先让定位模型探索生成坐标预测，再用MLLM-based Reflector评估预测一致性，输出对错标签+结构化推理反思
- 提出Reflection-Guided On-Policy Self-Distillation（R-OPSD）：将反思作为特权信息构建自教师模型，把文本类高层推理转化为坐标序列的token级监督信号，实现知识内化
- 设计Contrastive Calibration方法：针对失败探索中错误前缀导致的监督污染问题，引入反向提示学生模型与教师对比，抑制初始错误token、让漂移token的优势衰减到0，避免负向迁移；同时采用方向对齐的优势截断，结合GRPO的query级优势稳定训练
- 工程优化：定位模型和Reflector共享基座，通过切换LoRA适配器切换角色，3B模型仅需10GB显存

### 关键实验结果
在ScreenSpot、OSWorld-G等6个主流GUI基准测试，对比基线模型平均准确率提升7.4%，对比最新测试时RL方法GUI-RCPO最高提升7.7%；3B模型在未见过的SSv2数据集上准确率从50.2%提升到57.4%；R-OPSD的训练成本仅为传统GRPO的34%，优化效率提升近2倍。

### 核心结论
无需人工标注的测试时自进化是降低Agent部署后适配成本、实现持续迭代的核心路径，将文本反思转化为细粒度监督信号比稀疏奖励RL的优化效率更高、适配效果更好。
