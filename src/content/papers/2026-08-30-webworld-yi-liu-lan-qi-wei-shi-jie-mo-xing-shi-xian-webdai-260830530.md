---
title: 'WebWorld: The Browser as a World Model for Self-Improving Web Code'
title_zh: WebWorld：以浏览器为世界模型实现Web代码自改进
authors:
- Jiajun Wu
- Jian Yang
- Yaxin Du
- Wei Zhang
- Haowen Wang
- Junhang Cheng
- Yuxuan Zhang
- Tuney Zheng
- Xianglong Liu
- Ming Zhou
affiliations:
- Beihang University
- IQuest Research
- Shanghai Jiao Tong University
- Langboat
arxiv_id: '2608.30530'
url: https://arxiv.org/abs/2608.30530
pdf_url: https://arxiv.org/pdf/2608.30530
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: Agent 自改进闭环验证优化
tags:
- Agent
- World Model
- VLM
- Self-Improvement
- Code Generation
one_liner: 将浏览器作为不可欺骗的世界模型验证器，构建VLM生成Web代码的自改进闭环
practical_value: '- 做Agent工具调用/代码生成类业务时，可复用「用真实执行器做验证而非模型自评分」的思路，避免幻觉，比如电商活动页生成后用浏览器自动校验交互逻辑，降低人工审核成本

  - 自迭代闭环中可加入「历史能力留存校验」的质量棘轮机制，避免优化新需求时破坏已上线功能，比如推荐系统规则迭代时自动校验历史召回准确性不下降

  - 自训练数据筛选时，仅保留经过真实环境验证的合格样本做SFT，避免噪声样本拉低模型效果，可复用在生成式推荐文案、搜索Query改写的模型迭代流程中'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
VLM驱动的Web代码自改进存在结构性缺陷：生成修复的模型同时负责效果评判，视觉合理性无法等价于页面实际交互可用，自评分幻觉严重，迭代收益极低。
### 方法关键点
1. 提出WebWorld框架，将浏览器作为VLM无法欺骗的世界模型，提供确定性的代码执行验证能力
2. 每轮迭代将VLM的修改诉求编译为交互合约，浏览器验证通过的标准为：目标功能达成 + 所有历史已验证能力无退化，仅合格样本进入SFT训练集，形成质量棘轮
### 关键结果
- WebWorld-27B相比同规格Raw-27B，HTMLBench-400提升5.3分，MiniAppBench-Val提升14.9分，交互HTML生成能力达Kimi-K2.6、GPT-5.4等前沿系统水平
- 消融实验显示，移除浏览器认证环节后，9B模型的迭代收益几乎完全消失
