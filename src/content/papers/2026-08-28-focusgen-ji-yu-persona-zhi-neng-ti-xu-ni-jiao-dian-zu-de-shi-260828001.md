---
title: 'FocusGen: Expanding Visual Design Exploration with a Simulated Focus Group
  of Persona Agents'
title_zh: FocusGen：基于 persona 智能体虚拟焦点组的视觉设计探索系统
authors:
- Jaewon Choi
- Helena Vasconcelos
- Hyun Lee
- Carolyn Zou
- Tak Yeon Lee
- Michael Bernstein
affiliations:
- Hanwha Life
- Stanford University
- KAIST
arxiv_id: '2608.28001'
url: https://arxiv.org/abs/2608.28001
pdf_url: https://arxiv.org/pdf/2608.28001
published: '2026-08-28'
collected: '2026-08-31'
category: Agent
direction: Persona 多智能体 · 创意生成辅助
tags:
- Persona Agent
- Generative Design
- Multi-Agent
- Text-to-Image
- Creativity Support
one_liner: 通过虚拟 persona 智能体并行生成视觉设计，突破现有生成工具受限于设计师固有视角的局限
practical_value: '- 电商营销素材、广告创意生成场景可复用多Persona Agent并行生成架构，针对不同目标用户群生成分众创意，相比通用生成
  baseline 视觉多样性提升58%，可大幅拓展创意探索边界

  - 早期创意发散阶段，对Agent的偏好引导用开放式提问替代结构化问题，可提升生成结果多样性27%~30%，适合快速脑暴多种创意方向

  - 可复用「偏好引导→迭代自精炼→全序列TrueSkill排序选优」的 pipeline，提升生成结果与目标人群偏好的匹配度，真人验证中选优结果的偏好得分是零样本生成的2倍以上

  - 正式投放/真人调研前，可先用虚拟Persona Agent做创意快速校验，提前过滤低接受度方案，降低真人测试成本，需注意提示Agent规避刻板印象输出'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前文生图创意工具的探索边界完全受限于设计师的输入，仅能覆盖「已知的未知」，无法发现设计师认知外的创意方向；而真人焦点组、用户访谈的成本高、周期长，不适合早期高频率的创意发散阶段。

### 方法关键点
- 构建包含1000个Persona Agent的Agent Bank，每个Agent基于真实人口普查数据生成人口属性，搭配程序化生成的个人背景故事，具备稳定独立的身份特征
- 设计师输入设计需求后，可通过开放式/结构化问题访谈Agent，获取其针对需求的个性化美学偏好，生成标准化Persona Profile
- 每个Agent独立运行迭代生成回路：根据Profile生成初始图→对比自身偏好输出critique→修正prompt重生成，最多迭代5次，最终通过TrueSkill排序从全生成序列中选择最优结果
- 多Agent并行生成，最终输出匹配不同人群偏好的设计集合，设计师可通过筛选人群维度、调整访谈问题定向探索创意方向

### 关键实验
- 27名真人用户验证迭代回路效果：最终选择的精炼图片TrueSkill得分平均为15.57，是零样本生成（7.30）的2.13倍，用户选择精炼结果的概率显著高于随机基线
- 与通用助手baseline对比：Persona Agent生成的图片集合平均CLIP距离提升58%，人类感知评估中参与者认为Agent生成集合多样性更高的占比达86%
- 访谈方式对比：开放式提问相比结构化提问，人类生成结果的CLIP距离提升30%，Agent生成结果提升27%；但Agent的绝对多样性比真人 cohort 低27%左右

### 最值得记住的一句话
虚拟Persona焦点组是拓展创意边界的脚手架，仅可作为真人调研的前置补充，不能替代真实用户反馈，且需持续警惕模型输出的人口统计学刻板印象风险
