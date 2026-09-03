---
title: 'OmegaUse-SOP: SOP Engineering for Professional Computer Use from Human Demonstrations'
title_zh: OmegaUse-SOP：从人类演示构建专业计算机操作的SOP工程系统
authors:
- Yixiong Xiao
- Lang An
- Hucheng Yang
- Pinxue Ma
- Yongquan Chen
- Jingjia Cao
- Yusai Zhao
- Ting Wang
- Ting Liu
- Siqi Bao
affiliations:
- Baidu, Inc.
- Ningxia Electric Power Engineering Co., Ltd.
arxiv_id: '2609.02149'
url: https://arxiv.org/abs/2609.02149
pdf_url: https://arxiv.org/pdf/2609.02149
published: '2026-09-02'
collected: '2026-09-03'
category: Agent
direction: GUI Agent · 专业领域SOP落地
tags:
- GUI Agent
- SOP Engineering
- Human-in-the-loop
- Vision-Language Model
- Workflow Automation
one_liner: 提出四模块人在环SOP工程框架，将人类专业GUI操作演示转化为Agent可复用技能
practical_value: '- 电商/广告运营类重复SOP（如后台商品上下架、投放账户调价、数据报表导出）可直接复用这套「录演示→转语义步骤→配参数→执行验证」流程落地，无需对接零散API。

  - Reason模块的低阶操作转语义指令思路可直接复用，解决界面布局变化、分辨率差异导致的操作重放失败问题，大幅提升GUI Agent的环境适配性。

  - 执行阶段分步加载SOP信息+每步界面校验的逻辑可套用到长流程Agent任务，既避免全量SOP挤占上下文窗口，又能及时拦截操作错误，减少级联故障。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有GUI Agent在通用计算机任务上进展显著，但专业领域操作依赖隐含领域知识、软件特定规则、任务级校验要求，纯靠大模型自主推理容易出现步骤遗漏、参数错误、流程漂移等问题，无法稳定复现专业SOP，难以落地工业场景。

### 方法关键点
- **Observe模块**：记录人类操作的多模态GUI轨迹，包含操作前截图、鼠标键盘事件、UI元素bounding box，区分坐标类点击操作和非坐标类输入/快捷键操作。
- **Reason模块**：用VLM将低阶操作事件转化为语义步骤指令，给坐标点击补充操作对象、视觉上下文描述，给键盘操作补充操作场景和目的，避免盲放固定坐标。
- **Configure模块**：支持人在环补充领域规则、配置任务可变参数，将单次固定演示转化为可适配不同任务实例的通用SOP。
- **Execute模块**：分步加载当前步骤相关的SOP信息，降低上下文开销，每步执行后对比预期界面做结果校验，支持人工介入修正异常。

### 关键结果
基于电力行业光伏仿真软件PVsyst 7.2的5个真实SOP任务测试：无SOP指导时Qwen3-VL、GPT-5.5、Opus-4.7的任务通过率分别为20%、60%、40%；使用OmegaUse-SOP后，三者通过率均达到100%。 ablation实验显示去掉Reason模块后，Qwen3-VL的通过率从100%降至40%，验证了语义抽象对SOP复用的核心价值。

**最值得记住的结论**：SOP工程可类比Prompt工程，通过迭代优化演示、执行规则、任务参数，即可快速把人类专业经验转化为Agent可稳定执行的技能，无需从零训练领域专属大模型。
