---
title: 'IntentWeaver: Sustaining Coherence across Evolving Intents in Human-AI Co-Writing'
title_zh: 《IntentWeaver：人机协同写作中演化意图的跨层级一致性维持》
authors:
- Yuanhao Zhang
- Xinru Cheng
- Baiqiao Zhang
- Xinqi Zhang
- Assem Zhunis
- Shuai Ma
- Xiaojuan Ma
affiliations:
- The Hong Kong University of Science and Technology
- Peking University
- Santa Clara University
- Institute of Software, Chinese Academy of Sciences
arxiv_id: '2611.08214'
url: https://arxiv.org/abs/2611.08214
pdf_url: https://arxiv.org/pdf/2611.08214
published: '2026-11-05'
collected: '2026-11-07'
category: Agent
direction: 人机协同Agent 意图一致性维持
tags:
- Human-AI Collaboration
- Intent Tracking
- Coherence Maintenance
- Interactive Agent
- Writing Assistant
one_liner: 提出跨层级意图追踪工具IntentWeaver，解决人机协同写作中的高层意图漂移问题
practical_value: '- 意图层级建模方法可迁移到电商文案生成Agent：给文案设定品牌调性/活动目标/商品卖点多层级意图，自动校验生成文案的跨层级一致性，减少不符合品牌要求的输出

  - 意图漂移检测机制可复用在个性化推荐场景：追踪用户长短期意图的层级关系，当短期行为与长期兴趣出现偏差时主动校验，避免推荐结果偏离用户核心诉求

  - 意图演化的反馈传播逻辑可用于搜索Query理解：随着用户搜索交互迭代更新意图层级，自动将上层意图调整传导到下层Query改写逻辑，提升召回结果匹配度'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
人机协同写作场景下，AI生成的密集草稿易让用户陷入局部编辑，导致高层核心意图被忽略、低层生成内容漂移，出现意图不一致问题，现有工具未对意图演化做跨层级追踪。
### 方法关键点
1. 自动从草稿和用户交互中提取多层级意图图谱，覆盖从核心目标到具体措辞的全层级意图
2. 每次内容变更时，自动评估各层级意图的满足度与跨层级一致性
3. 支持意图变更的跨层级后果传播，同步调整各层生成要求
### 关键结果数字
24人组内对照实验表明，用户对高层意图的复盘迭代频次显著提升，未察觉的意图偏差大幅减少，产出文本与核心意图的匹配度明显更优
