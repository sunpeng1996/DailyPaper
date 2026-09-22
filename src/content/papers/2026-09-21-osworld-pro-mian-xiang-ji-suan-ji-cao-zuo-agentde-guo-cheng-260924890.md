---
title: 'OSWorld-Pro: Process-based Evaluation for Computer Use Agents'
title_zh: OSWorld-Pro：面向计算机操作Agent的过程化评估基准
authors:
- Zhilin Wang
- Shaokun Zhang
- Yifan Zhang
- Hao Zhang
- Jin Xu
- Binfeng Xu
- Jian Hu
- Yunheng Zou
- Karan Sapra
- Andrew Tao
affiliations:
- NVIDIA
arxiv_id: '2609.24890'
url: https://arxiv.org/abs/2609.24890
pdf_url: https://arxiv.org/pdf/2609.24890
published: '2026-09-21'
collected: '2026-09-22'
category: Agent
direction: Agent 计算机操作评估基准
tags:
- Computer-Use-Agent
- Process-Evaluation
- Benchmark
- LLM-Judge
- GUI-Agent
one_liner: 提出首个面向计算机操作Agent的过程化评估基准，覆盖300+长周期任务与2800+顺序依赖子目标
practical_value: '- 长周期业务Agent（如电商运营自动化、客服工单处理）评估可复用子目标拆解思路，替代仅看最终结果的评估方式，精准定位失败环节，迭代效率提升30%以上

  - LLM-Judge选型可直接复用论文结论：预算有限时，小模型调高推理档位的效果优于大模型低推理档位，同效果下成本最多可降80%

  - GUI操作类Agent（如电商后台操作、素材处理Agent）调试可参考动作维度拆解方法，按点击/拖拽/键盘输入等维度拆分错误，快速定位坐标识别、操作逻辑问题

  - 计算机操作Agent优化可优先提升点击、键盘输入等基础操作准确率，再做多应用协同和跨环境适配，投入ROI更高'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Computer-Use Agent（CUA）评估仅校验最终交付结果，无法区分不同完成度的失败轨迹、定位具体失败根因，还存在reward hacking风险，在长周期多步骤任务下评估颗粒度极粗，无法有效支撑Agent性能迭代。
### 方法关键点
- 构建305个长周期CUA任务，平均单任务含9.2个顺序依赖子目标，覆盖31款应用、19个Linux发行版、13种桌面界面，单任务平均需协调3.45个应用，难度远高于现有OSWorld基准
- 累计67264条步骤级人工标注，覆盖每步对应的子目标、子目标可行性、步骤进展、子目标完成状态4个维度，标注一致性Cohen's κ>0.8
- 配套人类对齐的LLM-Judge评估链路，单轨迹一次API调用完成所有子目标的过程校验，大幅降低人工评估成本
### 关键结果
- 基准难度：SOTA模型Claude Opus 5在OSWorld-Pro上任务全完成率仅75.7%，低于其在OSWorld上的83.4%；开源模型最高全完成率仅55.1%，远低于其在OSWorld上的80%+水平
- LLM-Judge效果：GPT-5.6-Sol Max的子目标识别、完成状态判断准确率接近人类（绝对差距<3.3%），仅在可行性、进展判断上差距较大
- 失败模式：开源模型点击操作准确率仅39%-42%，远低于闭源模型的72%-92%；强模型如Claude Opus 5也存在大量子目标无关操作，最高单次卡壳59步
### 核心结论
长周期Agent的迭代优化中，过程维度的细粒度反馈价值远高于最终结果的对错判断
