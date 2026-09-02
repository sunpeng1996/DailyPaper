---
title: UI-Venus-2 Technical Report
title_zh: UI-Venus-2 通用多模态GUI基础智能体技术报告
authors:
- Venus Team
- Zhuohan Cai
- Haoxing Chen
- Jiaxuan Chen
- Weizhi Chen
- Changlong Gao
- Zhangxuan Gu
- Yuan Guo
- Yusong Hu
- Jianrong Jiang
affiliations:
- Ant Group
arxiv_id: '2609.00028'
url: https://arxiv.org/abs/2609.00028
pdf_url: https://arxiv.org/pdf/2609.00028
published: '2026-08-26'
collected: '2026-09-02'
category: Agent
direction: GUI智能体 · 多端数字任务自动化
tags:
- GUI_Agent
- Multimodal
- Reinforcement_Learning
- Task_Automation
- Open_Source
one_liner: 开源跨移动端、网页、桌面的通用GUI基础智能体，多基准性能达同规模SOTA
practical_value: '- 可复用其「环境-任务-验证联合scaling」的工程框架，快速搭建电商域GUI自动化Agent，覆盖商家后台操作、APP运营、用户服务等跨端重复任务场景

  - 两级（trace-level+sample-level）验证的视觉关键点+多模型投票方案，可直接迁移到Agent执行效果自动验收环节，降低GUI交互任务的人工标注成本70%以上

  - 多教师On-policy Distillation的结构化动作感知蒸馏策略，适合异构任务下的Agent能力融合，无需为单场景维护独立模型，降低部署成本

  - 开源的9B/27B权重可直接基于LoRA微调，适配电商爬虫、订单处理、CAPTCHA自动识别等高频场景，小模型也能满足端侧部署需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有GUI Agent多针对基准数据集优化，落地时存在三大痛点：环境覆盖局限于少量应用、生成任务与实际应用功能脱节、奖励验证粗糙易被hack，无法适配移动端、网页、桌面多端真实场景的自动化需求。
### 方法关键点
- 统一闭环推理-动作框架，覆盖170+多语言移动APP、网页、原生桌面OS三类异构环境
- 采用深度研究驱动的功能对齐指令生成pipeline，结合动态更新的应用能力目录，确保生成任务可执行、贴合真实功能
- 两级验证机制：trace-level用任务相关视觉关键点+多模型投票判断整体任务完成度，sample-level做单步动作正确性校验，为RL训练提供可靠无偏的奖励信号
- 三阶段训练pipeline：多模态中训注入GUI交互知识、分域离线RL优化专项能力、多教师On-policy Distillation（MOPD）融合异构能力，新增动作感知蒸馏加权策略，重点监督动作部分的训练效果
### 关键结果
在20+主流GUI Agent基准上测试，同规模模型性能全面领先：27B版本在WebVoyager达93.4%，超GPT-5 SoM 2.8个百分点；VenusBench-Mobile达48.7%，超Claude-Opus-4.6 12.2个百分点；VenusBench-CAPTCHA达79.9%，超通用VLM最优26.9个百分点；9B小模型可保留27B版本85%以上核心能力，适合轻量化部署。
### 核心结论
GUI Agent落地的核心不是单点优化动作预测准确率，而是要将环境覆盖、任务构造、奖励验证三个环节联合迭代优化，才能适配真实复杂场景。
