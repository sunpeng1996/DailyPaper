---
title: 'The AI Wave and the Reinvention of Game Discovery: Oversupply, Structural
  Correction, and Agentic Player-Game Matching'
title_zh: AI浪潮下游戏发现机制重塑：供给过剩、结构修正与智能玩家-游戏匹配
authors:
- Brian Dean Madanamootoo
affiliations:
- University of Silicon Valley, California, USA
arxiv_id: '2607.25010'
url: https://arxiv.org/abs/2607.25010
pdf_url: https://arxiv.org/pdf/2607.25010
published: '2026-07-27'
collected: '2026-07-30'
category: Agent
direction: Agent 游戏推荐冷启动优化
tags:
- LLM Agent
- Recommender System
- Cold Start
- Player Modeling
- Platform Economics
one_liner: 量化AI驱动游戏市场供给冲击，提出人格化Agent冷启动匹配方案效果超随机基线2.7倍
practical_value: '- 可复用LLM persona agent的方向反转思路：将原先用于模拟用户评估推荐系统的persona agent直接作为匹配机制，降低冷启动场景下对交互数据的依赖

  - 供给过剩场景下的推荐系统设计可参考：除传统行为信号外，引入心理人格特征、社区UGC信号作为冷启动匹配特征，提升长尾/新品分发效率

  - 平台收益分配设计可复用其仿真思路：将匹配精度与分账规则联动建模，验证二者共同作用对供给侧创作者收入的提升效果

  - 可借鉴其用上游AIGC工具发布速度作为内容供给量的领先预测指标，提前调整推荐系统的冷启动策略储备'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
AI辅助游戏生产大幅降低开发门槛，引发游戏平台供给爆炸，Steam日均新增60款游戏，头部1%作品占据73.5%总时长，传统基于热度、交互信号的推荐系统完全无法覆盖长尾新品的冷启动分发需求，同时市场普遍担忧供给过剩会重演1983年北美游戏市场崩溃，亟需可规模化的匹配机制解决供给过剩下的内容发现效率问题。

### 方法关键点
- 量化供给冲击：基于93073款Steam元数据、20万条用户交互数据、itch.io目录数据计算注意力集中度，首次提出Hugging Face游戏资产生成模型发布速度作为供给量领先预测指标
- 结构对比：对比1983年游戏崩溃与当前市场结构，验证当前为收入集中而非系统性崩溃，核心差异为数字分发、收入多元化、整合资本充足三大因素
- 匹配机制创新：反转现有LLM persona agent的应用方向，将原本用于模拟用户评估推荐系统的persona agent直接作为匹配核心，输入玩家心理人格画像、行为信号、社区UGC信号三重特征，生成带可解释理由的推荐列表，支持玩家手动修正画像
- 收益仿真：控制相同收入池变量，对比4种分账结构下匹配精度对开发者中位数收入的影响

### 关键实验
冷启动试点基于真实Steam交互数据，完全未进入训练集的新品作为测试集，persona匹配在top10命中率达31.2%，是随机基线的2.7倍，结果经20次随机拆分和genre标签消融验证鲁棒；收益仿真显示，当前匹配精度下，再分配型分账结构可将开发者中位数收入从250美元提升至1400-2900美元，匹配精度进一步提升后所有分账结构的中位数收入均突破千美元。

### 核心结论
供给过剩场景下，推荐系统的核心矛盾已经从匹配已有热门内容转向挖掘长尾新品的用户适配性，基于人格的Agent匹配是可规模化替代人工编审的可行路径。
