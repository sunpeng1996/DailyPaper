---
title: Can LLM Agents Stick to the Script? A Benchmark for Long-Horizon Consistency
  in Interactive Narratives
title_zh: LLM智能体能否遵守设定？交互式叙事长程一致性基准NCP-Bench
authors:
- Yingpeng Ma
- Jianhao Yan
- Bei Shi
- Ka Hou Kam
- Runnan Wang
- Xuebo Liu
- Yulong Chen
- Yue Zhang
- Derek F. Wong
affiliations:
- University of Macau
- Westlake University
- Harbin Institute of Technology, Shenzhen
- University of Cambridge
- University of Aberdeen
arxiv_id: '2608.08160'
url: https://arxiv.org/abs/2608.08160
pdf_url: https://arxiv.org/pdf/2608.08160
published: '2026-08-07'
collected: '2026-08-13'
category: Agent
direction: Agent 长程逻辑一致性评测
tags:
- LLM Agent
- Long-Horizon Consistency
- Benchmark
- Interactive Narrative
- Automatic Evaluation
one_liner: 提出叙事承诺保持任务与NCP-Bench基准，量化测评交互式叙事下LLM的长程逻辑一致性
practical_value: '- 可复用「事实账本+固定承诺集+独立审计模块」的架构解决多轮交互Agent的一致性问题，比如电商导购Agent避免前后优惠规则矛盾、客服Agent不违背品牌服务承诺

  - 可借鉴对抗式压力测试方案，上线前用自动生成的极端用户输入（如薅羊毛话术、故意篡改历史对话的试探）测评Agent，提前发现逻辑漏洞降低线上故障

  - 长程Agent选型可参考实验结论：分层记忆架构能显著降低承诺冲突率，但要避免记忆过度压缩导致丢失用户输入细节，平衡一致性和响应相关性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM驱动的多轮交互智能体普遍存在长程逻辑不一致问题，面对用户自由输入时经常违背已确立的事实、规则约束，现有评估多为主观偏好打分，无法客观量化逻辑一致性缺陷，亟需可自动审计的标准化基准。
### 方法关键点
- 形式化定义Narrative Commitment Preservation（NCP）任务，要求智能体在多轮交互中不违反已确立的事实、不变量约束、事件顺序约束，同时达成预设目标
- 构建NCP-Bench基准，从覆盖18种类型的100部经典电影剧情摘要中提取结构化叙事规范：包含初始事实账本、三类承诺集（不变量/顺序/成就）、参考剧情轨迹
- 设计全自动评估框架：独立审计模块每轮自动检查事实冲突、承诺冲突、用户输入忽略三类问题，更新交互状态，无需人工介入
- 引入对抗玩家Agent，生成符合角色视角的挑战性输入，最大化暴露模型一致性缺陷
### 关键实验
在6个SOTA LLM上测评，GPT-5.2性能最优，20轮交互后存活率仅42%，事实冲突率40%；其他模型事实冲突率达40%~68%，几乎没有模型能在100轮内达成所有成就承诺；分层记忆Agent HiAgent可将平均交互轮数从22.16提升到30.05，承诺冲突率从26%降到4%，但用户输入忽略率从13%升至38%。
### 核心结论
LLM的语言流利度不代表长程逻辑一致性，当前模型缺乏显式的承诺保持机制，无法满足多轮交互场景下的可靠性要求
