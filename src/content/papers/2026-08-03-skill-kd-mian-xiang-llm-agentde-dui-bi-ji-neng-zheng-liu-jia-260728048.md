---
title: 'SKILL-KD: Contrastive Skill Distillation for LLM Agents'
title_zh: SKILL-KD：面向LLM Agent的对比技能蒸馏框架
authors:
- Qiming Shi
- Yibo Dou
- Jiawen Zhu
- Yulong Tao
- Linbo Jin
- Zhaolu Kang
- Yunfan Zhou
- Di Weng
affiliations:
- Zhejiang University
- Peking University
- Alibaba Group
arxiv_id: '2607.28048'
url: https://arxiv.org/abs/2607.28048
pdf_url: https://arxiv.org/pdf/2607.28048
published: '2026-08-03'
collected: '2026-08-06'
category: Agent
direction: Agent 技能蒸馏与知识库治理
tags:
- Skill Distillation
- LLM Agent
- Knowledge Distillation
- Skill Library
- Contrastive Learning
one_liner: 通过强弱Agent轨迹对比蒸馏可复用文本技能，无需微调学生模型即可提效
practical_value: '- 电商导购/客服Agent技能沉淀可复用「强弱轨迹对比→生成技能补丁→实测验证」pipeline，无需微调小模型即可对齐大模型的操作策略，快速提升业务效果

  - 技能库治理可照搬漂移感知 consolidation 机制：给每条技能加trace关联来源轨迹，新增技能时回溯历史避免重复、冲突、过拟合单case，降低技能库冗余60%以上

  - 中小模型落地Agent场景时，可直接用该框架从GPT-4/Claude等商用大模型蒸馏业务专属技能，无需重训小模型就能大幅降低推理成本

  - 搜索query纠错/推荐话术规则系统迭代，也可复用该「迭代验证+历史回溯」思路，避免规则反复修改导致的效果漂移'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent技能获取方案存在两类缺陷：从自身失败轨迹反思缺少正确策略指引，直接总结强教师的成功轨迹又过于抽象，和弱学生的行为模式不匹配；同时频繁新增局部修复的技能容易导致漂移、冗余，技能复用性差，且现有知识蒸馏方案需要更新学生模型参数，落地成本高。

### 方法关键点
- 以文本化可执行技能为蒸馏载体，对比强弱Agent同任务的轨迹差生成技能补丁，学生模型全程冻结，不需要参数更新
- 自适应技能蒸馏：生成候选补丁后重跑学生验证效果，失败就基于新的错误迭代优化补丁，只有验证通过的补丁才进入技能库
- 漂移感知技能整合：给每条技能加溯源trace（关联来源轨迹、修改历史），新增补丁时回溯历史，决策是新增/修改/删除/跳过补丁，避免技能库膨胀和规则冲突

### 关键实验
在5个Agent基准（SearchQA、SpreadsheetBench、DocVQA、LiveMath、ALFWorld）上测试，两组师生配置：Qwen3.5-4B学生+Qwen3.7-plus教师，Qwen3.6-35B学生+ChatGPT-5.5教师，对比NoSkill、EvoSkill、Trace2Skill等基线。第一组平均得分从43.5%提升到66.8%，第二组从57.9%提升到74.6%；最终技能库仅38条规则，比学生自反思方案少60%。

### 核心结论
技能蒸馏的核心是对齐目标学生的行为模式，而非单纯复刻教师的操作逻辑，基于行为验证的对比蒸馏能得到更紧凑、适配性更强的可复用技能
