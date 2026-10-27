---
title: 'Evolving to Match Capabilities: Improving Harness Self-Evolution via Skill
  Adaptation'
title_zh: 能力适配式进化：通过技能适配提升Harness自进化效果
authors:
- Zhihao Yang
- Haojin Wang
- Juncheng Wu
- Kuan Zhang
- Yukun Chen
- Run Luo
- Yaojie Lu
- Yuyin Zhou
- Lu Wang
- Xianpei Han
affiliations:
- University of Chinese Academy of Sciences
- Tsinghua University
- University of California, Santa Cruz
- National University of Singapore
- Institute of Software, Chinese Academy of Sciences
arxiv_id: '2610.33024'
url: https://arxiv.org/abs/2610.33024
pdf_url: https://arxiv.org/pdf/2610.33024
published: '2026-10-09'
collected: '2026-10-27'
category: Agent
direction: LLM Agent 技能适配与自进化优化
tags:
- LLM Agent
- Self-Evolution
- Skill Adaptation
- Harness
- Meta-Skill
one_liner: 提出通用元技能指导技能改写，适配不同能力LLM Agent，提升Harness自进化性能
practical_value: '- 搭建Agent系统时不要用统一技能模板，需针对部署的LLM能力（开源小模型/商用大模型）定制技能，对弱模型需将技能拆解为「动作-目标-完成条件」的明确格式，避免抽象描述。

  - 可复用论文的4类失败诊断框架（工具执行/上下文管理/指令遵循/校验），快速定位弱模型Agent任务失败根因，针对性优化Prompt或技能模板。

  - 自建Agent自进化闭环时，给模型提供固定的元技能改写规则，无需修改模型参数，即可让弱模型稳定从执行反馈中优化技能，避免进化漂移。

  - 电商场景的导购Agent、售后Agent的流程模板可参考技能适配思路，针对不同能力的坐席/大模型定制话术和流程规则，提升执行准确率。'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Harness自进化方案默认技能可跨模型通用，但实际发现同一技能对强模型增益极高，对弱模型甚至可能带来负向效果：103个任务-技能对中，技能让GPT-5.6-luna提升31.1分，却让Gemma-4-E4B下降8.8分；86%的弱模型失败案例中，要求已经明确写在技能里但模型未遵循，因此需要针对执行者能力做技能适配，让技能和模型能力匹配才能发挥价值。

### 方法关键点
- 先诊断弱模型执行失败的4类核心模式：工具执行失败（调用不存在的工具、报错不恢复）、上下文管理混乱（把技能示例当任务、输出路径错误）、指令遵循不足（遗漏技能里明确的要求）、校验缺失（输出错误无自查）
- 设计固定的任务无关元技能，将4类失败模式转化为明确改写规则：工具执行部分明确可调用工具列表+错误处理方案；上下文部分开头先明确任务范围和交付路径，与参考材料做区隔；指令部分每个要求拆解为「动作-目标-完成条件」；校验部分增加独立结果检查步骤
- 支持两种落地模式：① 用强模型作为改写器，基于元技能一次性改写技能，不需要执行轨迹；② 集成到自进化闭环，每轮执行后模型基于轨迹和反馈，用元技能自行改写技能

### 关键实验结果
基于SkillsBench、DocOps、Tessl三个基准筛选的103个技能敏感任务-技能对，覆盖7个不同能力层级的LLM：强改写器Kimi-K3基于元技能改写的技能，让3个弱模型得分提升5.1~14.1分；集成到5轮自进化闭环后，所有7个模型得分比无元技能的基线高2.0~5.1分。

### 最值得记住的一句话
Harness的效果不是Harness本身的属性，而是和执行者能力的匹配度共同决定的，技能要适配模型能力才能发挥价值。
