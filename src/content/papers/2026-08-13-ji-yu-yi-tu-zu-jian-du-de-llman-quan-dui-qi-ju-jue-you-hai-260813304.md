---
title: 'Refusing Intent, Not Form: Wrapper-Based Intent-Group Supervision for LLM
  Safety'
title_zh: 基于意图组监督的LLM安全对齐：拒绝有害意图而非表面形式
authors:
- Ping Wu
- Haibo Tong
- Feifei Zhao
- Han Shen
- Yu Shi
- Yilin Zhao
- Sicheng Shen
- Guobin Shen
- Yun Luo
- Yi Zeng
affiliations:
- 中国科学院自动化研究所BrainCog实验室
- 中国科学院大学人工智能学院
- 北京市安全人工智能与超对齐重点实验室
- 蚂蚁集团
arxiv_id: '2608.13304'
url: https://arxiv.org/abs/2608.13304
pdf_url: https://arxiv.org/pdf/2608.13304
published: '2026-08-13'
collected: '2026-08-14'
category: LLM
direction: LLM安全对齐 · 意图组监督训练
tags:
- LLM-Safety
- Alignment
- Jailbreak-Defense
- Over-Refusal
- LoRA
one_liner: 提出意图组数据增强与双路线训练策略，兼顾LLM越狱防御与低良性请求误拒
practical_value: '- 做电商导购/客服Agent安全对齐时，可复用WIFA的无标注数据构造思路，将相同意图的不同问法配对生成训练集，大幅降低安全标注成本

  - 业务需要平衡安全与用户体验时，可借鉴A-GCRT的组一致性正则，强制同意图不同表述的输出决策一致，既拦截恶意话术变种，又减少正常咨询的误拒

  - 可直接复用双路线训练框架，根据场景需求选安全优先（公域客服）或低误拒优先（会员助手）的策略，无需重构全量训练数据'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM安全微调易学到表面形式捷径：攻击者通过角色伪装、学术讨论、虚拟场景等包装的有害prompt可绕过防御，而结构相似的良性请求反而被过度拒绝，现有方案要么防御能力不足，要么严重牺牲用户体验，亟需兼顾防越狱和低误拒的对齐方法。
### 方法关键点
- WIFA数据增强：将相同意图的不同表面包装归为一组，配对构造同包装的有害、良性意图组，无需外部教师模型或手动标注，自动生成训练数据，让包装形式无法作为拒绝决策的依据
- 双训练路线：WIFA-Boost为两阶段LoRA SFT，先学习意图-形式分离，再校准拒绝边界，主打高安全防御；A-GCRT在SFT基础上加入组一致性正则+锚定损失，让同意图不同包装的决策得分一致，同时将有害/良性意图的得分推到阈值两侧，主打低过度拒绝
- 轻量决策信号：取意图分析标记后的首个token logit，计算拒绝前缀与合规前缀的最大logit差作为决策依据，无需额外分类器
### 关键实验
在Qwen2.5-7B、Llama3.1-8B上测试，对比6种现有基线。Qwen场景下，WIFA-Boost将SORRY-Bench变种平均拒答率从22.1提升至63.7，为所有方案最高；A-GCRT-M5将OR-Bench过度拒绝率从25.7降至17.4，低于基线与原生模型，同时保持46.7的有害请求拒答率，通用能力损失极小；15种未见过的越狱攻击测试中，WIFA-Boost平均攻击成功率仅9.5%。
### 核心结论
LLM安全对齐的核心是拒绝有害意图，而非表面话术形式。
