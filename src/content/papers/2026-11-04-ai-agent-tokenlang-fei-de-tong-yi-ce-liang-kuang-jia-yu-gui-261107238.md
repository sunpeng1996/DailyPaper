---
title: How Do AI Agents Waste Your Money?
title_zh: AI Agent token浪费的统一测量框架与归因分析
authors:
- Huimin Zeng
- Yuxuan Lu
- Jesse Cai
- Eric Hanchen Jiang
- Di Wu
- Po-Nien Kung
- Wenbo Hu
- Ziyi Wang
- Dakuo Wang
- Jiaxin Pei
affiliations:
- University of Illinois Urbana-Champaign
- Northeastern University
- University of California, Los Angeles
- UT Austin
arxiv_id: '2611.07238'
url: https://arxiv.org/abs/2611.07238
pdf_url: https://arxiv.org/pdf/2611.07238
published: '2026-11-04'
collected: '2026-11-06'
category: Agent
direction: Agent 运行时token效率优化
tags:
- AI Agent
- Token Efficiency
- LLM-as-a-Judge
- Agent Harness
- Cost Optimization
one_liner: 提出跨异构Agent系统的token浪费统一测量框架，可在基本不影响性能的前提下修剪41-46%的推理token
practical_value: '- 可复用文中LLM-as-a-Judge的浪费识别规则，针对电商导购Agent、广告文案生成Agent等业务场景，在线修剪restate/duplicate-fetch/padding三类严格浪费，可在基本不影响效果的前提下降低40%左右推理成本

  - 优化Agent harness时优先排查环境配置类问题（如工具参数不匹配、运行环境错误），这类重试导致的浪费属于完全可避免的严格浪费，无需调整模型即可快速降低token消耗

  - 不要盲目调高Agent推理档位，推理强度超过阈值后性能不再提升但token成本大幅上涨，可根据业务价值分级配置推理档位，平衡效果与成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前AI Agent多轮交互的token成本极高，但现有成本优化仅以总token用量为核心指标，无法区分必要消耗和可移除的冗余浪费，盲目压缩token容易损害任务效果；同时异构Agent系统的轨迹、计费规则不统一，缺少系统化的token浪费测量与归因方法，难以定位降本空间。
### 方法关键点
- 轻量接入：基于代理层统一拦截异构Agent的请求与响应，标准化轨迹格式，仅需少量代码修改即可接入现有Agent系统，无需改动原有业务逻辑
- 分类定义浪费：明确四类浪费模式，将可直接移除的restate（重复已有上下文）、duplicate-fetch（重复拉取不变信息）、padding（无意义填充话术）归为严格浪费，将事后可跳过的探索性行为归为detour类可优化浪费
- 可验证测量：用LLM-as-a-Judge标注浪费片段，通过移除片段后重跑Agent的方式验证可移除性，基于模型厂商原生计费规则计算实际浪费金额，避免规则误判影响效果
### 关键结果
在4个Agent基准、6个前沿LLM上验证：在线修剪严格浪费可移除41-46%的推理token，任务成功率基本无下降；整体Agent输出token中平均18%为浪费，45%的任务中单个Agent的浪费量超过另一个完成同任务Agent的总token消耗；token浪费差异更多来自任务、harness设计，而非LLM选型，相同LLM和任务下不同harness的token用量最多差4倍。
### 核心结论
降低Agent成本的核心不是盲目压缩总token用量，而是精准识别可移除的浪费部分，多数场景下优化harness设计、匹配合理推理档位的降本效果优于更换小模型。
