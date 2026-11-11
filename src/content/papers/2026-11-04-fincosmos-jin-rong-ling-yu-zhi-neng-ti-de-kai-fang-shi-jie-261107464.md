---
title: 'FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance'
title_zh: FINCOSMOS：金融领域智能体的开放世界评估范式
authors:
- Yupeng Cao
- Xueqing Peng
- Lingfei Qian
- Haohang Li
- Yangyang Yu
- Anke Xu
- Wenbo Cao
- Yan Wang
- Yuechen Jiang
- Yuyan Wang
affiliations:
- The Fin AI
- Stevens Institute of Technology
- University of Manchester
- MBZUAI
- University of Montreal
arxiv_id: '2611.07464'
url: https://arxiv.org/abs/2611.07464
pdf_url: https://arxiv.org/pdf/2611.07464
published: '2026-11-04'
collected: '2026-11-11'
category: Eval
direction: Agent 开放世界评估范式设计
tags:
- Agent
- Evaluation
- Open-World
- Finance
- LLM Agent
one_liner: 提出面向金融领域Agent的无标准答案开放世界评估范式，可精准检测Agent隐性故障
practical_value: '- 可借鉴无标准答案评估设计：电商导购/投流类Agent评估可引入隐藏用户需求+多维度自动校验逻辑，替代依赖人工标注标准答案的传统模式，适配开放场景隐性故障检测

  - 可迁移否决校验框架：面向业务Agent的效果验证可复用15项否决校验的设计思路，从数据时效性、策略匹配度、结果可复现性三个维度做自动化校验

  - 可复用反馈优化路径：基于评估反馈直接迭代Agent持久记忆模块的训练方式，快速提升复杂交互任务的完成率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有金融Agent评估基准均为封闭世界设定，固定任务、数据或时间线，无法检测Agent隐性故障（如策略不匹配、数据未验证、回测使用未来数据等），适配开放Web场景的可信评估能力缺失。
### 方法关键点
提出FINCOSMOS开放世界评估范式：1. 模拟用户持有从组合语法采样的隐藏策略，仅在被询问时披露；2. Agent无初始数据，需自主从Web获取数据、在数据截断约束下完成回测、输出可验证结果；3. 无需参考标准答案，通过程序校验数据时点正确性、复现指标、匹配隐藏策略，仅当用户满意且15项否决校验全通过才算合格。
### 关键结果
150次测试覆盖4个编码Agent和1个无工具模型，无一次通过；用户签字确认的会话全部未通过程序校验，Agent仅能覆盖54%~64%的未知需求细节，88.33%的故障归因于Agent本身；带持久记忆的Agent接入FINCOSMOS反馈后可完成全部10项任务
