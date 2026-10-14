---
title: 'Rubrics from the Task, Verdicts from Evidence: Pointwise Rubric Rewards with
  Tool-Augmented Judges'
title_zh: 基于任务评分规则与工具增强的逐点奖励模型ReVeR
authors:
- Tianci Liu
- Haoyu Wang
affiliations:
- University of Tennessee
- University at Albany
arxiv_id: '2610.18766'
url: https://arxiv.org/abs/2610.18766
pdf_url: https://arxiv.org/pdf/2610.18766
published: '2026-10-12'
collected: '2026-10-14'
category: Training
direction: LLM训练 · 逐点评分奖励模型
tags:
- Reward Model
- RLHF
- Rubric Evaluation
- Tool Augmentation
- Pointwise Reward
one_liner: 提出仅从指令生成规则、工具增强的逐点奖励模型ReVeR，4B参数性能优于8B成对评分RM
practical_value: '- 电商文案生成、Agent回答评估场景可复用「hard rules+分级principles」双轨架构：硬规则（违禁词、字数、格式约束）用代码直接校验，主观质量用LLM打分，避免纯LLM评估的机械错误

  - 训练自定义Reward Model时可采用label-blind蒸馏方法：仅用偏好标签做样本过滤，不修改教师模型的推理轨迹，降低标注偏置，提升RM泛化性

  - 推荐多目标排序可借鉴其聚合逻辑：先做硬性约束（合规、价格区间、地域限制）截断过滤，再用偏好/质量分排序，避免核心规则被体验分突破

  - 做LLM/Agent对齐时优先选择逐点RM，其输出的独立分数可直接作为GRPO等在线RL的奖励信号，省去成对偏好转奖励的适配成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有rubric-based reward models（RMs）存在三大痛点：一是规则从候选响应反向推导，引入响应偏置，泛化性差；二是纯LLM法官难以准确校验字数、格式、正则匹配等机械约束，容易出错；三是常用的成对RM仅输出相对偏好，无法直接作为奖励信号用于策略优化，落地门槛高。

### 方法关键点
- 规则生成模块仅基于指令推理，拆分出强制满足的hard rules（0/1打分）和分级质量principles（0-100分），规则仅与任务本身绑定，与候选响应无关
- 逐点工具增强法官：每个响应独立评估，机械类约束自动调用Python解释器执行校验，语义类约束用LLM推理打分
- 采用label-blind蒸馏训练：教师模型仅用学生侧可见的输入生成推理轨迹，偏好标签仅做样本过滤，不修改轨迹内容，产出ReVeR-Traces数据集（含30K规则推理、61K工具评估轨迹）
- 奖励聚合采用字典序逻辑：先计算硬规则满足数，同分再用原则平均分分档，确保硬性要求不被突破

### 关键结果
4B参数的ReVeR在11个RM基准上平均偏好准确率达69.1%，超过8B参数的成对RM Rubric-ARM（66.3%），指令跟随类任务准确率领先最多13.1个百分点；基于ReVeR做DPO训练，7B基座模型的IFEval平均得分从53.9提升到57.9，比8B成对RM训练效果高2.4个百分点；Best-of-16选点时IFEval准确率达85.1，比最强基线高3.7个百分点。

### 核心结论
rubric fidelity、preference accuracy、downstream utility是奖励模型的三个独立属性，需要分别评估，不可互相替代。
