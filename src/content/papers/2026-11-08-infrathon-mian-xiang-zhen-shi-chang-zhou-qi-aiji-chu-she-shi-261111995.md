---
title: 'Infrathon: Benchmarking Language Agents for Real-World, Long-Horizon AI Infra
  Optimization'
title_zh: Infrathon：面向真实长周期AI基础设施优化的语言Agent基准
authors:
- Zhengyu Hu
- Zheyuan Xiao
- Yike Wang
- Hamish Ivison
- Haoyu Wang
- Yige Yuan
- Rulin Shao
- Yuetai Li
- Niqi Lyu
- Yicheng Ding
affiliations:
- University of Washington
- Allen Institute for AI
- University of Pennsylvania
- Stanford University
- Northwestern University
arxiv_id: '2611.11995'
url: https://arxiv.org/abs/2611.11995
pdf_url: https://arxiv.org/pdf/2611.11995
published: '2026-11-08'
collected: '2026-11-11'
category: Agent
direction: 长周期Agent · AI基建优化基准
tags:
- Long-horizon Agent
- Benchmark
- AI Infrastructure
- KV Cache
- Code Agent
one_liner: 推出覆盖算子/模块/系统三级的25个长周期AI基建优化Agent基准，验证长周期评估的价值
practical_value: '- 做长周期Agent任务评估可复用Work-Controller-Judge三层架构，通过私有测试+合规校验避免奖励黑客，适配推荐全链路优化、大模型推理优化等业务场景的Agent评测

  - 电商/广告场景的LLM推理服务可直接借鉴论文中Claude输出的KV cache优化方案，将压缩比从6.8×提升到19.8×，大幅降低推理时延和GPU成本

  - 长周期优化任务的资源分配可参考论文结论：算子级任务适合短周期多轮次测试，模块/系统级任务需预留充足运行时长，避免过早终止错过后期性能增益

  - Agent选型需匹配任务周期：短周期快速迭代任务优先选前期表现更优的GPT-6 Astra类模型，长周期深度优化任务优先选后期增益更高的Claude Opus类模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有AI基础设施优化Agent的评测基准普遍存在任务覆盖不全、运行时长短等问题，仅能反映Agent短周期内的单次优化能力，无法匹配真实场景下基建优化需要长期迭代、多轮验证的需求，短周期评估容易漏掉后期性能增益，也会导致错误的模型性能排序。
### 方法关键点
- 构建覆盖算子、模块、系统三个层级的25个真实AI基建优化任务，算子级任务配置12小时运行预算，模块、系统级任务配置24小时运行预算，覆盖训练、推理两类场景的常见优化需求
- 采用三层隔离执行架构：Work环境供Agent迭代代码、运行公开测试；Controller层做指令合规校验，防止奖励黑客行为；Judge层运行私有测试返回反馈，不泄露测试集与评分逻辑
- 配套Infrathon-build工具，支持用户快速自定义适配自身业务的长周期优化任务
### 关键结果
累计投入超10000 GPU小时，测试6款前沿大模型共150次运行：135次运行在预算后半段仍能获得性能提升，其中33次运行后半段增益超10%；Claude Opus 5.5在17个任务上夺冠，其优化的Quant-VideoGen KV codec平均压缩比从人工设计的6.82×提升至19.86×，同时视频质量优于人工方案；模型排名随评估时长动态变化，GPT-6 Astra在25%预算时排名第一，Claude Opus 5.5在50%预算后反超并保持第一。
最值得记住的一句话：长周期任务下模型的相对性能会随评估时长发生显著变化，短周期评估不仅会遗漏潜在优化增益，还会导致错误的模型选型决策。
