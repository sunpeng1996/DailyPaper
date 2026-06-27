---
title: 'Running the Gauntlet: Re-evaluating the Capabilities of Agents Beyond Familiar
  Environments'
title_zh: GauntletBench：陌生复杂场景下的Agent能力重评估基准
authors:
- Mykola Vysotskyi
- Runqi Lin
- Grzegorz Biziel
- Michal Zakrzewski
- Sebastian Montagna
- Damian Rynczak
- Shreyansh Padarha
- Kumail Alhamoud
- Zihao Fu
- William Lugoloobi
affiliations:
- University of Oxford
- SoftServe
- Massachusetts Institute of Technology
- The Chinese University of Hong Kong
- UK AI Security Institute
arxiv_id: '2606.14397'
url: https://arxiv.org/abs/2606.14397
pdf_url: https://arxiv.org/pdf/2606.14397
published: '2026-06-24'
collected: '2026-06-27'
category: Agent
direction: Agent 复杂场景泛化能力评估基准
tags:
- Web Agent
- Agent Benchmark
- Multimodal Reasoning
- Generalization
- Evaluation
one_liner: 提出覆盖5类专业应用100个视觉密集任务的Web Agent基准，探测三类被忽视的Agent能力
practical_value: '- 电商/广告投放Agent评估可复用「规则化定制评估器 + MLLM进度评分」双轨方案：对视频剪辑、3D商品建模、投放流程搭建这类视觉/操作密集任务，核心指标用带公差的规则校验（如视频时长±100ms、颜色模糊匹配），中间进度用MLLM判分，比纯精确匹配更贴合业务实际

  - 通用Computer Use Agent在非标准化画布类（如3D建模、流程图、视频轨）任务上成功率不足20%，业务落地（如商家后台自动化、素材生产Agent）需优先对这类图形/3D/时序操作做领域微调或工具封装，不能直接依赖通用Agent能力

  - 复杂长流程Agent的动作规划可采用「分治式细粒度增量步骤」策略：实验显示该策略虽步骤数更多，但整体成功率和token效率更优，适合电商运营、广告投放这类多步操作场景的Agent设计'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent基准多搭建于电商、CRM等大众熟悉的应用之上，任务以表单填写、信息检索等简单操作为主，能力覆盖集中在UI理解、工具调用等基础维度，导致前沿Agent性能快速饱和，无法真实反映复杂专业场景下的泛化能力短板。尤其是时间感知、图形理解、3D推理三类对复杂场景至关重要的能力，长期被现有评估体系忽视，亟需更具挑战性的基准来探测Agent的真实能力边界。

### 方法关键点
- 任务设计：聚焦三类未被充分探索的核心能力（时间感知、图形理解、3D推理），搭建5个小众专业Web应用（视频编辑器、工作流构建器、3D建模器、航班分析器、电路设计器），共100个视觉密集型任务；每个应用含2易9中9难共20个任务，多数场景仅提供画布截图，限制DOM/无障碍树访问，强制Agent依赖视觉感知完成任务
- 架构设计：采用模块化Web环境，通过Playwright提供高层动作接口（点击、输入、滚动等），统一兼容开源MLLM Agent、API型MLLM、闭源Agent框架三类系统
- 评估体系：搭配定制化领域评估器（如视频编辑支持100ms时长公差、颜色模糊匹配，航班分析支持集合无序匹配），同时输出三类指标：全或无的成功率、MLLM评判的1-5分进度率、token/步骤数效率指标

### 关键实验
测试14个前沿Agent，覆盖开源MLLM、API MLLM、闭源Computer Use Agent三类，对比非专业人类标注者：
- SOTA闭源Agent（Claude Opus 4.6 Computer Use）平均成功率仅19.1%，Gemini Enterprise为13.7%，GPT-5.4 CU仅4.3%；开源MLLM几乎全部接近0%
- 非专业人类标注者平均成功率达80.8%，且执行步骤数比SOTA Agent少30%
- 视觉模态可显著提升任务进度率，Qwen、GPT系列在支持视觉后进度率分别提升43.5%、15.5%；模型规模提升可同时改善性能并降低总token消耗

### 最值得记住的一句话
当前Agent在熟悉场景的表现具有很强的迷惑性，一旦进入陌生的专业视觉操作场景，其真实能力与人类仍有数量级差距
