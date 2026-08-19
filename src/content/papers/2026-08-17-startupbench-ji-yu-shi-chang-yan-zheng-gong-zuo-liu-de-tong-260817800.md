---
title: 'StartupBench: Benchmarking General-Purpose Agents on Market-Validated End-to-End
  Workflows'
title_zh: StartupBench：基于市场验证工作流的通用Agent基准测试
authors:
- Liya Zhu
- Xin Ma
- Tao Liu
- Haodong Wang
- Ge Zhang
- Jingzhe Ding
- Qingshui Gu
- Yongjie Zhong
- Jinxiang Meng
- Yuan Gao
affiliations:
- ByteDance Seed
- Nanjing University
- M-A-P
- TokenWave.AI
arxiv_id: '2608.17800'
url: https://arxiv.org/abs/2608.17800
pdf_url: https://arxiv.org/pdf/2608.17800
published: '2026-08-17'
collected: '2026-08-19'
category: Agent
direction: Agent 端到端专业工作流能力评测
tags:
- Agent-Benchmark
- E2E-Workflow
- General-Purpose-Agent
- Agent-as-Judge
- Vertical-Agent
one_liner: 构建了源自市场验证AI创业产品场景的端到端通用Agent工作流评测基准
practical_value: '- 垂直领域Agent评测可复用其任务构建逻辑：从已商业化落地的付费用户需求倒推任务定义，而非研究员自造场景，避免评测完全脱离业务实际

  - 复杂多格式交付物评测可复用rubric-wise Agent-as-Judge方案，单条评估维度对应独立Judge会话，比整体一次性打分和专家标注的一致性高10%左右，执行稳定性更强

  - 业务Agent选型可参考核心结论：通用Agent和垂直优化Agent的交付成功率差11pct以上，强规则类业务（如电商合规、广告审核）优先选择垂直优化Agent

  - Agent落地故障排查可复用其失败分析框架：优先检查复杂指令完整遵循、核心规则合规、输出格式匹配三类高频问题，可覆盖80%以上的常见故障'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent基准多由研究员人工定义任务，既脱离真实用户付费场景的实际需求，也缺乏对复杂多格式交付物的细粒度评估能力，无法准确衡量Agent在商业化落地场景下的实际可用性，难以指导业务落地选型。

### 方法关键点
- 任务采集：筛选融资超100万美元、有真实用户付费的AI原生创业公司产品，通过30+深度用户访谈还原真实工作流，由50+领域专家标准化为可复现的评测任务
- 评估设计：采用rubric-wise Agent-as-Judge方案，每个细粒度评估维度对应独立Judge会话，覆盖功能、结构、格式、域合规等6个维度，平均每个任务对应25.3条评估规则
- 数据集构成：覆盖医疗、金融、法律、商业管理等6个领域共97个任务，支持DOCX/XLSX/PPTX/PDF等多种主流办公交付格式

### 关键结果
- 测试9款主流闭源/开源模型，最强模型平均得分73.67%，但满足90分以上可直接交付标准的成功率仅31.27%，远低于平均得分
- 自动评测和专家标注的一致性达92.8%，比整体一次性打分的评测方案一致性高近10个百分点
- 通用Agent和垂直优化Agent的交付成功率差距达11.12pct，性能瓶颈主要集中在复杂指令完整遵循、领域专业知识合规、计算精度三个方面

**最值得记住的一句话**：当前通用Agent的最大瓶颈不是完成大部分工作流，而是持续产出无需人工校验即可直接交付的专业成果。
